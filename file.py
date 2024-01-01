import csv


def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w", encoding='utf-8-sig', newline='') #encoding넣어줘야 한글 안깨짐! newline=''은 CSV 파일에서 빈 행을 피하기 위한 옵션.
    writer = csv.writer(file)
    writer.writerow(["Position", "Company", "Location", "Link"])

    for job in jobs:
        writer.writerow(job.values())
    file.close()