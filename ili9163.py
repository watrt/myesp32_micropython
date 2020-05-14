
import time
from micropython import const
import framebuf
font={
    0x0020:[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    0x0021:[0x00, 0x00, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x00, 0x20, 0x00, 0x00],
    0x0022:[0x00, 0x28, 0x50, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    0x0023:[0x00, 0x00, 0x28, 0x28, 0xFC, 0x28, 0x50, 0xFC, 0x50, 0x50, 0x00, 0x00],
    0x0024:[0x00, 0x20, 0x78, 0xA8, 0xA0, 0x60, 0x30, 0x28, 0xA8, 0xF0, 0x20, 0x00],
    0x0025:[0x00, 0x00, 0x48, 0xA8, 0xB0, 0x50, 0x28, 0x34, 0x54, 0x48, 0x00, 0x00],
    0x0026:[0x00, 0x00, 0x20, 0x50, 0x50, 0x78, 0xA8, 0xA8, 0x90, 0x6C, 0x00, 0x00],
    0x0027:[0x00, 0x40, 0x40, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    0x0028:[0x00, 0x04, 0x08, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x08, 0x04, 0x00],
    0x0029:[0x00, 0x40, 0x20, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x20, 0x40, 0x00],
    0x002A:[0x00, 0x00, 0x00, 0x20, 0xA8, 0x70, 0x70, 0xA8, 0x20, 0x00, 0x00, 0x00],
    0x002B:[0x00, 0x00, 0x20, 0x20, 0x20, 0xF8, 0x20, 0x20, 0x20, 0x00, 0x00, 0x00],
    0x002C:[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x40, 0x80],
    0x002D:[0x00, 0x00, 0x00, 0x00, 0x00, 0xF8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    0x002E:[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x00],
    0x002F:[0x00, 0x08, 0x10, 0x10, 0x10, 0x20, 0x20, 0x40, 0x40, 0x40, 0x80, 0x00],
    0x0030:[0x00, 0x00, 0x70, 0x88, 0x88, 0x88, 0x88, 0x88, 0x88, 0x70, 0x00, 0x00],
    0x0031:[0x00, 0x00, 0x20, 0x60, 0x20, 0x20, 0x20, 0x20, 0x20, 0x70, 0x00, 0x00],
    0x0032:[0x00, 0x00, 0x70, 0x88, 0x88, 0x10, 0x20, 0x40, 0x80, 0xF8, 0x00, 0x00],
    0x0033:[0x00, 0x00, 0x70, 0x88, 0x08, 0x30, 0x08, 0x08, 0x88, 0x70, 0x00, 0x00],
    0x0034:[0x00, 0x00, 0x10, 0x30, 0x50, 0x50, 0x90, 0x78, 0x10, 0x18, 0x00, 0x00],
    0x0035:[0x00, 0x00, 0xF8, 0x80, 0x80, 0xF0, 0x08, 0x08, 0x88, 0x70, 0x00, 0x00],
    0x0036:[0x00, 0x00, 0x70, 0x90, 0x80, 0xF0, 0x88, 0x88, 0x88, 0x70, 0x00, 0x00],
    0x0037:[0x00, 0x00, 0xF8, 0x90, 0x10, 0x20, 0x20, 0x20, 0x20, 0x20, 0x00, 0x00],
    0x0038:[0x00, 0x00, 0x70, 0x88, 0x88, 0x70, 0x88, 0x88, 0x88, 0x70, 0x00, 0x00],
    0x0039:[0x00, 0x00, 0x70, 0x88, 0x88, 0x88, 0x78, 0x08, 0x48, 0x70, 0x00, 0x00],
    0x003A:[0x00, 0x00, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x20, 0x00, 0x00],
    0x003B:[0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x20, 0x20, 0x00],
    0x003C:[0x00, 0x04, 0x08, 0x10, 0x20, 0x40, 0x20, 0x10, 0x08, 0x04, 0x00, 0x00],
    0x003D:[0x00, 0x00, 0x00, 0x00, 0xF8, 0x00, 0x00, 0xF8, 0x00, 0x00, 0x00, 0x00],
    0x003E:[0x00, 0x40, 0x20, 0x10, 0x08, 0x04, 0x08, 0x10, 0x20, 0x40, 0x00, 0x00],
    0x003F:[0x00, 0x00, 0x70, 0x88, 0x88, 0x10, 0x20, 0x20, 0x00, 0x20, 0x00, 0x00],
    0x0040:[0x00, 0x00, 0x70, 0x88, 0x98, 0xA8, 0xA8, 0xB8, 0x80, 0x78, 0x00, 0x00],
    0x0041:[0x00, 0x00, 0x20, 0x20, 0x30, 0x50, 0x50, 0x78, 0x48, 0xCC, 0x00, 0x00],
    0x0042:[0x00, 0x00, 0xF0, 0x48, 0x48, 0x70, 0x48, 0x48, 0x48, 0xF0, 0x00, 0x00],
    0x0043:[0x00, 0x00, 0x78, 0x88, 0x80, 0x80, 0x80, 0x80, 0x88, 0x70, 0x00, 0x00],
    0x0044:[0x00, 0x00, 0xF0, 0x48, 0x48, 0x48, 0x48, 0x48, 0x48, 0xF0, 0x00, 0x00],
    0x0045:[0x00, 0x00, 0xF8, 0x48, 0x50, 0x70, 0x50, 0x40, 0x48, 0xF8, 0x00, 0x00],
    0x0046:[0x00, 0x00, 0xF8, 0x48, 0x50, 0x70, 0x50, 0x40, 0x40, 0xE0, 0x00, 0x00],
    0x0047:[0x00, 0x00, 0x38, 0x48, 0x80, 0x80, 0x9C, 0x88, 0x48, 0x30, 0x00, 0x00],
    0x0048:[0x00, 0x00, 0xCC, 0x48, 0x48, 0x78, 0x48, 0x48, 0x48, 0xCC, 0x00, 0x00],
    0x0049:[0x00, 0x00, 0xF8, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0xF8, 0x00, 0x00],
    0x004A:[0x00, 0x00, 0x7C, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x90, 0xE0, 0x00],
    0x004B:[0x00, 0x00, 0xEC, 0x48, 0x50, 0x60, 0x50, 0x50, 0x48, 0xEC, 0x00, 0x00],
    0x004C:[0x00, 0x00, 0xE0, 0x40, 0x40, 0x40, 0x40, 0x40, 0x44, 0xFC, 0x00, 0x00],
    0x004D:[0x00, 0x00, 0xD8, 0xD8, 0xD8, 0xD8, 0xA8, 0xA8, 0xA8, 0xA8, 0x00, 0x00],
    0x004E:[0x00, 0x00, 0xDC, 0x48, 0x68, 0x68, 0x58, 0x58, 0x48, 0xE8, 0x00, 0x00],
    0x004F:[0x00, 0x00, 0x70, 0x88, 0x88, 0x88, 0x88, 0x88, 0x88, 0x70, 0x00, 0x00],
    0x0050:[0x00, 0x00, 0xF0, 0x48, 0x48, 0x70, 0x40, 0x40, 0x40, 0xE0, 0x00, 0x00],
    0x0051:[0x00, 0x00, 0x70, 0x88, 0x88, 0x88, 0x88, 0xE8, 0x98, 0x70, 0x18, 0x00],
    0x0052:[0x00, 0x00, 0xF0, 0x48, 0x48, 0x70, 0x50, 0x48, 0x48, 0xEC, 0x00, 0x00],
    0x0053:[0x00, 0x00, 0x78, 0x88, 0x80, 0x60, 0x10, 0x08, 0x88, 0xF0, 0x00, 0x00],
    0x0054:[0x00, 0x00, 0xF8, 0xA8, 0x20, 0x20, 0x20, 0x20, 0x20, 0x70, 0x00, 0x00],
    0x0055:[0x00, 0x00, 0xCC, 0x48, 0x48, 0x48, 0x48, 0x48, 0x48, 0x30, 0x00, 0x00],
    0x0056:[0x00, 0x00, 0xCC, 0x48, 0x48, 0x50, 0x50, 0x30, 0x20, 0x20, 0x00, 0x00],
    0x0057:[0x00, 0x00, 0xA8, 0xA8, 0xA8, 0x70, 0x50, 0x50, 0x50, 0x50, 0x00, 0x00],
    0x0058:[0x00, 0x00, 0xD8, 0x50, 0x50, 0x20, 0x20, 0x50, 0x50, 0xD8, 0x00, 0x00],
    0x0059:[0x00, 0x00, 0xD8, 0x50, 0x50, 0x20, 0x20, 0x20, 0x20, 0x70, 0x00, 0x00],
    0x005A:[0x00, 0x00, 0xF8, 0x90, 0x10, 0x20, 0x20, 0x40, 0x48, 0xF8, 0x00, 0x00],
    0x005B:[0x00, 0x38, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x38, 0x00],
    0x005C:[0x00, 0x40, 0x40, 0x40, 0x20, 0x20, 0x10, 0x10, 0x10, 0x08, 0x00, 0x00],
    0x005D:[0x00, 0x70, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x70, 0x00],
    0x005E:[0x00, 0x20, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    0x005F:[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFC],
    0x0060:[0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    0x0061:[0x00, 0x00, 0x00, 0x00, 0x00, 0x30, 0x48, 0x38, 0x48, 0x3C, 0x00, 0x00],
    0x0062:[0x00, 0x00, 0xC0, 0x40, 0x40, 0x70, 0x48, 0x48, 0x48, 0x70, 0x00, 0x00],
    0x0063:[0x00, 0x00, 0x00, 0x00, 0x00, 0x38, 0x48, 0x40, 0x40, 0x38, 0x00, 0x00],
    0x0064:[0x00, 0x00, 0x18, 0x08, 0x08, 0x38, 0x48, 0x48, 0x48, 0x3C, 0x00, 0x00],
    0x0065:[0x00, 0x00, 0x00, 0x00, 0x00, 0x30, 0x48, 0x78, 0x40, 0x38, 0x00, 0x00],
    0x0066:[0x00, 0x00, 0x1C, 0x20, 0x20, 0x78, 0x20, 0x20, 0x20, 0x78, 0x00, 0x00],
    0x0067:[0x00, 0x00, 0x00, 0x00, 0x00, 0x3C, 0x48, 0x30, 0x40, 0x78, 0x44, 0x38],
    0x0068:[0x00, 0x00, 0xC0, 0x40, 0x40, 0x70, 0x48, 0x48, 0x48, 0xEC, 0x00, 0x00],
    0x0069:[0x00, 0x00, 0x20, 0x00, 0x00, 0x60, 0x20, 0x20, 0x20, 0x70, 0x00, 0x00],
    0x006A:[0x00, 0x00, 0x10, 0x00, 0x00, 0x30, 0x10, 0x10, 0x10, 0x10, 0x10, 0xE0],
    0x006B:[0x00, 0x00, 0xC0, 0x40, 0x40, 0x5C, 0x50, 0x70, 0x48, 0xEC, 0x00, 0x00],
    0x006C:[0x00, 0x00, 0xE0, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0xF8, 0x00, 0x00],
    0x006D:[0x00, 0x00, 0x00, 0x00, 0x00, 0xF0, 0xA8, 0xA8, 0xA8, 0xA8, 0x00, 0x00],
    0x006E:[0x00, 0x00, 0x00, 0x00, 0x00, 0xF0, 0x48, 0x48, 0x48, 0xEC, 0x00, 0x00],
    0x006F:[0x00, 0x00, 0x00, 0x00, 0x00, 0x30, 0x48, 0x48, 0x48, 0x30, 0x00, 0x00],
    0x0070:[0x00, 0x00, 0x00, 0x00, 0x00, 0xF0, 0x48, 0x48, 0x48, 0x70, 0x40, 0xE0],
    0x0071:[0x00, 0x00, 0x00, 0x00, 0x00, 0x38, 0x48, 0x48, 0x48, 0x38, 0x08, 0x1C],
    0x0072:[0x00, 0x00, 0x00, 0x00, 0x00, 0xD8, 0x60, 0x40, 0x40, 0xE0, 0x00, 0x00],
    0x0073:[0x00, 0x00, 0x00, 0x00, 0x00, 0x78, 0x40, 0x30, 0x08, 0x78, 0x00, 0x00],
    0x0074:[0x00, 0x00, 0x00, 0x20, 0x20, 0x70, 0x20, 0x20, 0x20, 0x18, 0x00, 0x00],
    0x0075:[0x00, 0x00, 0x00, 0x00, 0x00, 0xD8, 0x48, 0x48, 0x48, 0x3C, 0x00, 0x00],
    0x0076:[0x00, 0x00, 0x00, 0x00, 0x00, 0xEC, 0x48, 0x50, 0x30, 0x20, 0x00, 0x00],
    0x0077:[0x00, 0x00, 0x00, 0x00, 0x00, 0xA8, 0xA8, 0x70, 0x50, 0x50, 0x00, 0x00],
    0x0078:[0x00, 0x00, 0x00, 0x00, 0x00, 0xD8, 0x50, 0x20, 0x50, 0xD8, 0x00, 0x00],
    0x0079:[0x00, 0x00, 0x00, 0x00, 0x00, 0xEC, 0x48, 0x50, 0x30, 0x20, 0x20, 0xC0],
    0x007A:[0x00, 0x00, 0x00, 0x00, 0x00, 0x78, 0x10, 0x20, 0x20, 0x78, 0x00, 0x00],
    0x007B:[0x00, 0x18, 0x10, 0x10, 0x10, 0x20, 0x10, 0x10, 0x10, 0x10, 0x18, 0x00],
    0x007C:[0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10],
    0x007D:[0x00, 0x60, 0x20, 0x20, 0x20, 0x10, 0x20, 0x20, 0x20, 0x20, 0x60, 0x00],
    0x007E:[0x40, 0xA4, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    0x007F:[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    0x4ECA:[0x04, 0x00, 0x0A, 0x00, 0x11, 0x00, 0x20, 0x80, 0xC8, 0x60, 0x04, 0x00, 0x00, 0x00, 0x7F, 0x80,
    0x00, 0x80, 0x01, 0x00, 0x02, 0x00, 0x04, 0x00],
    0x5929:[0x00, 0x00, 0x7F, 0xC0, 0x04, 0x00, 0x04, 0x00, 0x04, 0x00, 0xFF, 0xE0, 0x04, 0x00, 0x0A, 0x00,
    0x0A, 0x00, 0x11, 0x00, 0x20, 0x80, 0xC0, 0x60],
    0x597D:[0x20, 0x00, 0x27, 0xC0, 0x20, 0x40, 0xF8, 0x80, 0x49, 0x00, 0x49, 0x00, 0x4F, 0xE0, 0x91, 0x00,
    0x51, 0x00, 0x21, 0x00, 0x51, 0x00, 0x8B, 0x00],
    0x6C14:[0x20, 0x00, 0x3F, 0xE0, 0x40, 0x00, 0xBF, 0xC0, 0x00, 0x00, 0x7F, 0x80, 0x00, 0x80, 0x00, 0x80,
    0x00, 0x80, 0x00, 0xA0, 0x00, 0x60, 0x00, 0x20],
    0x771F:[0x04, 0x00, 0x7F, 0xC0, 0x04, 0x00, 0x3F, 0x80, 0x20, 0x80, 0x3F, 0x80, 0x20, 0x80, 0x3F, 0x80,
    0x20, 0x80, 0xFF, 0xE0, 0x11, 0x00, 0x20, 0x80],
}
class ILI9163(framebuf.FrameBuffer):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.buffer = bytearray(self.width * self.height *2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.init_display()

    def init_display(self):
        self.write_cmd(0x11) # Exit Sleep

        time.sleep_ms(20)

        self.write_cmd(0x26, [0x04]) # Set Default Gamma
        self.write_cmd(0xB1, [0x08,0x08]) # Set Frame Rate
        self.write_cmd(0xC0, [0x0a,0x02]) # Set VRH1[4:0] & VC[2:0] for VCI1 & GVDD
        self.write_cmd(0xC1, [0x03]) # Set BT[2:0] for AVDD & VCL & VGH & VGL
        self.write_cmd(0xC5, [0x4f,0x5a]) # Set VMH[6:0] & VML[6:0] for VOMH & VCOML

        self.write_cmd(0x3a, [0x55]) # Set Color Format, 5=16 bit,3=12 bit
        self.write_cmd(0x36, [0xc0]) # RGB

        self.write_cmd(0x2A, [0,0,0,self.width]) # Set Column Address
        self.write_cmd(0x2B, [0,0,0,self.height]) # Set Page Address

        self.write_cmd(0xB4, [0]) #  display inversion
        self.write_cmd(0xC7, [0x40])
        self.write_cmd(0xf2, [0x01]) # Enable Gamma bit
        self.write_cmd(0xE0, [0x3f,0x25,0x1c,0x1e,0x20,0x12,0x2a,0x90,0x24,0x11,0x00,0x00,0x00,0x00,0x00])
        self.write_cmd(0xE1, [0x20,0x20,0x20,0x20,0x05,0x00,0x15,0xa7,0x3d,0x18,0x25,0x2a,0x2b,0x2b,0x3a])
        
        self.write_cmd(0xB7, [0,0])

        self.write_cmd(0x29) #  Display On
        self.write_cmd(0x2C) #  reset frame ptr

        self.fill(0)
        self.show()

    def poweroff(self):
        pass

    def poweron(self):
        self.write_cmd(0x29)

    def contrast(self, contrast):
        pass

    def invert(self, invert):
        pass

    def show(self):
        x0 = 0
        x1 = self.width - 1

        y0 = 0
        y1 = self.height + 0 - 1

        self.write_cmd(0x2A, [x0, 0, x1])
        self.write_cmd(0x2B, [y0, 0, y1])
        self.write_cmd(0x2C)
        self.write_data(self.buffer)


class ILI9163_SPI(ILI9163):
    def __init__(self, width, height, spi, dc, res, cs):
        self.rate = 40 * 1024 * 1024
        
        dc.init(dc.OUT, value=0)
        res.init(res.OUT, value=0)
        cs.init(cs.OUT, value=1)
        self.spi = spi
        self.dc = dc
        self.res = res
        self.cs = cs

        self.res(1)
        time.sleep_ms(1)
        self.res(0)
        time.sleep_ms(10)
        self.res(1)

        super().__init__(width, height)

    def write_cmd(self, cmd, data=None):
        self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))

        if data != None:
            self.cs(1)
            self.dc(1)
            self.cs(0)
            self.spi.write(bytearray(data))
        self.cs(1)

    def write_data(self, buf):

        self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(buf)
        self.cs(1)
    def brg(self, r=0,b=0,g=0):
        return ((b & 0xF8) << 8) | ((r & 0xFC) << 3) | (g >> 3)
        
    def drawCircle(self,x,y,r,c):
        for i in range(360):
          ax=round(x+r*math.cos(math.radians(i)))
          ay=round(y+r*math.sin(math.radians(i)))
          self.pixel(ax,ay,c)
          
    def drawFillCircle(self,x,y,r,c):
        for i in range(360):
          ax=round(x+r*math.cos(math.radians(i)))
          ay=round(y+r*math.sin(math.radians(i)))
          self.line(x,y,ax,ay,c)
    def textch(self,str="", x=0, y=0,c=0x0000):
      for s in str:
        chr=font[ord(s)]
        if ord(s)<127:
          font_width=6
        else:
          font_width=12
        for i in range(12):

          code=0x00
          if font_width>8:
            code|=chr[2*i]<<8
            code|=chr[2*i+1]
          else:
            code|=chr[i]<<8
          print("{:08b}".format(code))
          for j in range(font_width):
            if code<<j & 0x8000:
              self.pixel(x+j,y+i,c)
        x+=font_width
# Convert RGB888 to BRG565
# ((b & 0xF8) << 8) | ((r & 0xFC) << 3) | (g >> 3)

# Sample code
# ===========

# HSPI = 1
# VSPI = 2

# from machine import Pin, SPI
# spi = SPI(VSPI, sck=Pin(18), mosi=Pin(23))

# ili = ILI9163_SPI(128, 128, spi, Pin(2), Pin(4), Pin(15))

# ili.text('Hello World', 0, 0, 1)















