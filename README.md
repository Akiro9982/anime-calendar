# 📅 Anime Calendar Automation

![GitHub Actions](https://img.shields.io/github/actions/workflow/status/Akiro9982/anime-calendar/update.yml?label=workflow&logo=github)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Active-brightgreen?logo=github)

---

## ✨ Descripción

Este repositorio contiene una **automatización personal** para generar un calendario dinámico de emisión de animes.  
El sistema obtiene la información desde **AniList**, la procesa con un script en **Python** y publica un archivo `.ics` en **GitHub Pages**, el cual se puede suscribir directamente en **Google Calendar**.

⚠️ **Nota importante:**  
Este proyecto está diseñado **exclusivamente para uso personal del propietario**. No está pensado como un servicio público ni como una herramienta de distribución masiva.

---

## 🔄 Flujo de Automatización

```text
   ┌───────────┐       ┌─────────────────┐       ┌───────────────┐       ┌─────────────────┐
   │   AniList │──────▶│ GitHub Actions  │──────▶│ GitHub Pages  │──────▶│Google Calendar│
   └───────────┘       └─────────────────┘       └───────────────┘       └─────────────────┘
        │                   │                          │                          │
        │ Obtención Animes  │  Ejecución script cada   │  Publica archivo         │  Se suscribe a la
        │  Horarios         │  6 horas                 │  anime_calendar.ics      │  URL y refresca
