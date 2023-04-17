from io import BufferedReader
import logging

logger = logging.getLogger()

def read(files: list, dumpname: str):
    with open(dumpname, 'rb') as dump:
        for file in files:
            try:
                filename = file.get("filename")
                if filename == None:
                    skip_sectors(file.get("end") - file.get("start"), 512, dump)
                else:
                    read_sector(file.get("end") - file.get("start"), 512, dump, filename)
            except KeyError:
                logger.exception(f"Can't read file {file}")

def read_sector(sectors: int, size: int, file: BufferedReader, writefile_name: str):
    with open(writefile_name, 'wb') as w:
        for _ in range(sectors):
            w.write(file.read(size))

def skip_sectors(sectors: int, size: int, file: BufferedReader):
    for _ in range(sectors):
        file.read(size)


if __name__ == "__main__":
    files = [
        {
            "start": 0,
            "end": 9999
        },
        {
            "filename": "09260002.jpg",
            "start": 10000,
            "end": 10058
        },
        {
            "filename": "100_0304crop.bmp",
            "start": 10059,
            "end": 15050
        },
        {
            "filename": "09260002.jpg",
            "start": 15051,
            "end": 15110
        },
        {
            "filename": "100_0304crop.bmp",
            "start": 15111,
            "end": 20103
        },
        {
            "start": 20104,
            "end": 30103
        },
        {
            "filename": "100_0018.tif",
            "start": 30104,
            "end": 39848
        },
        {
            "filename": "02010025.pcx",
            "start": 39849,
            "end": 40373
        },
        {
            "filename": "100_0018.tif",
            "start": 40374,
            "end": 50118
        },
        {
            "filename": "02010025.pcx",
            "start": 50119,
            "end": 50643
        },
        {
            "filename": "100_0018.tif",
            "start": 50644,
            "end": 60390
        },
        {
            "filename": "02010025.pcx",
            "start": 60391,
            "end": 60916
        },
        {
            "start": 60917,
            "end": 70916
        },
        {
            "filename": "100_0183.gif",
            "start": 70917,
            "end": 71045
        },
        {
            "filename": "000_0021.png",
            "start": 71046,
            "end": 83707
        },
        {
            "filename": "02010025.pcx",
            "start": 83708,
            "end": 84494
        },
        {
            "filename": "100_0183.gif",
            "start": 84495,
            "end": 84625
        },
        {
            "filename": "000_0021.png",
            "start": 84626,
            "end": 97289
        },
        {
            "filename": "02010025.pcx",
            "start": 97290,
            "end": 98078
        }
    ]

    read(files=files, dumpname="L5_Graphic.dd")
