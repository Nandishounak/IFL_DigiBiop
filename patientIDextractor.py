import os


def pat_id_extractor(path):
    for file in os.listdir(path):
        d=os.path.join(path, file)
        if os.path.isdir(d):
            # print(d)
            x = d.split('\\')
            print(x[-1])

    # for it in os.scandir(path):
    #     if it.is_dir():
    #         print(it.path)
    # print(type(it))


if __name__ == '__main__':
    pat_id_extractor("C:\\Users\\shoun\\OneDrive - TUM\\Downloads\\patientdata_yr_19\\19\\")