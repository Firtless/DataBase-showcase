# Лабораторна робота №4: REST API для ветеринарної клініки (`vet_clinic_db`)

Розробка Back-End REST API сервісу на мові Python з використанням мікрофреймворку **Flask** та ORM **SQLAlchemy** для бази даних ветеринарної клініки (Варіант 32).

---

## 🛠 Технологічний стек

- **Language:** Python 3.15+
- **Framework:** Flask
- **ORM:** SQLAlchemy
- **Database:** MySQL
- **DB Driver:** PyMySQL
- **API Testing:** Postman

---

## 🏛 Архітектура проєкту (5-Layer Architecture)

Проєкт розроблено із чітким розділенням відповідальності за 5-рівневою паттерн-архітектурою:

```text
[HTTP Request] ──> Route ──> Controller ──> Service ──> DAO ──> Domain (SQLAlchemy) ──> [MySQL Database]
```
