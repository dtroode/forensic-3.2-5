from io import BufferedReader
import logging

logger = logging.getLogger()
cursor = 0

def read(files: list, dumpname: str):
    with open(dumpname, 'rb') as dump:
        for file in files:
            try:
                read_file(writefile_name=file["filename"], sectors=file["sectors"], sector_size=512, file=dump)
            except KeyError:
                logger.exception(f"Can't read file {file}")

def read_file(writefile_name, sectors, sector_size, file):
    with open(writefile_name, 'ab') as w:
        w.truncate(0)
        for sector in sectors:
            sectors_count = sector["end"] - sector["start"] + 1

            file.seek(sector["start"] * sector_size)
            print(sector["start"] * sector_size)

            for _ in range(sectors_count):
                w.write(file.read(sector_size))
    


if __name__ == "__main__":
    files = [
        {
            "filename": "09260002.jpg",
            "sectors": [
                {
                    "start": 10000,
                    "end": 10058
                },
                {
                    "start": 15051,
                    "end": 15110
                }
            ]
            
        },
        {
            "filename": "100_0304crop.bmp",
            "sectors": [
                {
                    "start": 10059,
                    "end": 15050
                },
                {
                    "start": 15111,
                    "end": 20103
                }
            ]
        },
        {
            "filename": "100_0018.tif",
            "sectors": [
                {
                    "start": 30104,
                    "end": 39848
                },
                {
                    "start": 40374,
                    "end": 50118
                },
                {
                    "start": 50644,
                    "end": 60390
                }
            ]
        },
        {
            "filename": "02010025.pcx",
            "sectors": [
                {
                    "start": 39849,
                    "end": 40373
                },
                {
                    "start": 50119,
                    "end": 50643
                },
                {
                    "start": 60391,
                    "end": 60916
                },
                {
                    "start": 83708,
                    "end": 84494
                },
                {
                    "start": 97290,
                    "end": 98078
                }
            ]
        },
        {
            "filename": "100_0183.gif",
            "sectors": [
                {
                    "start": 70917,
                    "end": 71045
                },
                {
                    "start": 84495,
                    "end": 84625
                }
            ]
        },
        {
            "filename": "000_0021.png",
            "sectors": [
                {
                    "start": 71046,
                    "end": 83707
                },
                {
                    "start": 84626,
                    "end": 97289
                }
            ]
        },
    ]

    read(files=files, dumpname="/Users/fedorprozorov/Library/Mobile Documents/com~apple~CloudDocs/expert_analiz/6/L5_Graphic.dd")
