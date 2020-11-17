#!/usr/bin/python
# encoding: utf-8
# 汉字点阵显示

RECT_HEIGHT = RECT_WIDTH = 16
BYTE_COUNT_PER_ROW = RECT_WIDTH // 8
BYTE_COUNT_PER_FONT = BYTE_COUNT_PER_ROW * RECT_HEIGHT
KEYS = [0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01]


class FontRender(object):
    def __init__(self, font_file,
                 rect_height=RECT_HEIGHT, rect_width=RECT_WIDTH, byte_count_per_row=BYTE_COUNT_PER_ROW):
        self.font_file = font_file
        self.rect_height = rect_height
        self.rect_width = rect_width
        self.byte_count_per_row = byte_count_per_row
        self.__init_rect_list__()

    def __init_rect_list__(self):
        self.rect_list = [] * RECT_HEIGHT
        for i in range(RECT_HEIGHT):
            self.rect_list.append([] * RECT_WIDTH)

    def get_font_area_index(self, txt):
        gbk = txt.encode('gbk')
        hex_str = list(gbk)
        area = hex_str[0] - 0xA0
        index = hex_str[1] - 0xA0
        return area, index

    def get_font_rect(self, area, index):
        offset = (94 * (area - 1) + (index - 1)) * BYTE_COUNT_PER_FONT
        with open(self.font_file, "rb") as f:
            f.seek(offset)
            btxt = f.read(BYTE_COUNT_PER_FONT)
        return btxt

    def convert_font_rect(self, font_rect, ft=1, ff=0):
        font_rect = list(font_rect)
        for k in range(len(font_rect) // self.byte_count_per_row):
            row_list = self.rect_list[k]
            for j in range(self.byte_count_per_row):
                for i in range(8):
                    asc = font_rect[k * self.byte_count_per_row + j]
                    flag = asc & KEYS[i]
                    row_list.append(flag and ft or ff)

    def render_font_rect(self, rect_list=None):
        if not rect_list:
            rect_list = self.rect_list
        for row in rect_list:
            for i in row:
                if i:
                    print('■', end=' ')
                else:
                    print('○', end=' ')
            print()

    def convert(self, text_list, ft=None, ff=None):
        for t in text_list:
            area, index = self.get_font_area_index(t)
            font_rect = self.get_font_rect(area, index)
            self.convert_font_rect(font_rect, ft=ft, ff=ff)

    def get_rect_info(self):
        return self.rect_list


if '__main__' == __name__:
    text = '盛泽中学'
    fr = FontRender('./font/hzk{}'.format(RECT_WIDTH))
    fr.convert(text, ft='/static/*', ff=0)
    fr.render_font_rect()
