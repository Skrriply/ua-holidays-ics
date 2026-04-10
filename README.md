# 🇺🇦 Ukrainian Holidays

A Python script that scrapes official holiday data from [the website of the Verkhovna Rada of Ukraine](https://zakon.rada.gov.ua/laws/main/days/sps) and generates an `.ics` file.

While originally designed for import into [Proton Calendar](https://proton.me/calendar), the resulting file fully works with [Google Calendar](https://calendar.google.com/), [Apple Calendar](https://support.apple.com/guide/calendar/welcome/mac), [Outlook](https://outlook.live.com/calendar/), and more.

## 📅 How to subscribe

Add the link below to your calendar:

```
https://raw.githubusercontent.com/Skrriply/ua-holidays-ics/refs/heads/main/calendar.ics
```

Guides for popular services:

- [Proton Calendar](https://proton.me/support/subscribe-to-external-calendar#subscribe)
- [Google Calendar](https://support.google.com/calendar/answer/37100)
- [Apple Calendar](https://support.apple.com/en-us/102301)
- [Outlook](https://support.microsoft.com/en-us/office/import-or-subscribe-to-a-calendar-in-outlook-com-or-outlook-on-the-web-cff1429c-5af6-41ec-a5b4-74f2c278e98c)

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
