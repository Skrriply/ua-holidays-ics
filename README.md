# 🇺🇦 Ukrainian Holidays

A Python script that scrapes official holiday data from [the website of the Verkhovna Rada of Ukraine](https://zakon.rada.gov.ua/laws/main/days/sps) and generates an `.ics` file.

While originally designed for import into [Proton Calendar](https://proton.me/calendar), the resulting file fully works with [Google Calendar](https://alternativeto.net/outgoing/software/google-calendar), [Apple Calendar](https://support.apple.com/guide/calendar/welcome/mac), [Outlook](https://outlook.live.com/calendar/), and more.

## 🧰 Installation

### 1. Clone the repository:

```bash
git clone https://github.com/Skrriply/ua-holidays-ics.git
cd ua-holidays-ics
```

### 2. Install dependencies:

It is recommended to use `uv` for managing dependencies.

This project uses:
- `httpx` for requests
- `beautifulsoup4` and `lxml` for parsing
- `icalendar` for file generation.

```bash
python -m pip install uv
uv sync
```

## 🚀 Usage

To generate the calendar file, simply run the main script:

```bash
uv run ./src/app/main.py
```


## ⚖️ License

This project is licensed under the [GPL-3.0 License](https://github.com/Skrriply/ua-holidays-ics/blob/main/LICENSE).
