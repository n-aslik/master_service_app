import subprocess
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--http', help='Описание аргумента http')
args = parser.parse_args()

print(args.http)

# Настройки
FASTAPI_HOST = "127.0.0.1"
FASTAPI_PORT = "8000"

def run_fastapi():
    print("🚀 Запускаем FastAPI...")
    return subprocess.Popen([
        "uvicorn", "main:app",
        "--host", FASTAPI_HOST,
        "--port", FASTAPI_PORT
    ])

def run_pinggy():
    print("🌐 Подключаем Pinggy...")
    return subprocess.Popen([
       "python", "-m", "pinggy", "--http", f"{FASTAPI_HOST}:{FASTAPI_PORT}"
    ])

def main():
    fastapi_proc = run_fastapi()
    time.sleep(2)  # Дать FastAPI время на запуск
    pinggy_proc = run_pinggy()

    try:
        print("✅ Всё запущено. Нажми Ctrl+C для остановки.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Останавливаем процессы...")
        fastapi_proc.terminate()
        pinggy_proc.terminate()

if __name__ == "__main__":
    main()

