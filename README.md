# Ethiopian Medical Data Platform (Kara Solutions)

An end-to-end data engineering solution to extract, transform, enrich, and analyze data about Ethiopian medical businesses from public Telegram channels.

---

## Project Goals

This platform is designed to:
- Identify the top 10 most frequently mentioned medical products.
- Analyze price and availability trends across Telegram channels.
- Detect and classify medical images (e.g., pills, creams) using YOLO.
- Monitor posting volume trends daily and weekly.
- Serve cleaned data and analytics via a FastAPI interface.

---

## Tech Stack

- **Python** – Core programming language
- **Telethon / Pyrogram** – Telegram scraping
- **PostgreSQL** – Data warehouse
- **dbt** – Transformation and modeling
- **YOLOv8** – Object detection on images
- **FastAPI** – API for serving analytics
- **Docker (optional)** – Containerization
- **GitHub Actions** – CI/CD pipeline

---

## Project Structure

