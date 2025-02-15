import os
import time


def delete_previously_uploaded_files(current_dir, file_ext='.exe') -> None:
    """Удаление всех ранее загруженных файлов"""
    for filename in os.listdir(current_dir):
        if filename.endswith(file_ext):
            file_path = os.path.join(current_dir, filename)
            try:
                os.remove(file_path)  # Удаление файла
            except Exception as e:
                print(f"Не удалось удалить файл {file_path}: {e}")


def wait_for_download_file(work_dir, file_ext='.exe') -> None:
    """Ожидание загрузки файла"""
    while True:
        if any([filename.endswith(file_ext) for filename in os.listdir(work_dir)]):
            break
        time.sleep(0.5)


def file_exists(directory, filename) -> bool:
    """Проверка существования файла"""
    file_path = os.path.join(directory, filename)
    file_status = os.path.isfile(file_path)
    return file_status
