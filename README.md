# Voice Chatbot UAS

**Pemrosesan Bahasa Alami • Semester Genap 2024/2025**

Sebuah aplikasi chatbot berbasis suara yang memungkinkan pengguna berbicara melalui antarmuka web. Sistem akan:

1. Menerima input suara pengguna (Speech-to-Text)
2. Mengolah teks melalui model bahasa besar (Google Gemini API)
3. Mengembalikan respons dalam bentuk suara (Text-to-Speech)

---

## Fitur Utama

* **Speech-to-Text (STT)**
  * Menggunakan `whisper.cpp` dari OpenAI untuk mentranskripsi audio `.wav` ke teks.

* **LLM Integration**
  * Memanfaatkan Google Gemini API untuk menghasilkan respons dalam Bahasa Indonesia.

* **Text-to-Speech (TTS)**
  * Menggunakan model Coqui TTS (v1.2) dengan speaker `wibowo` untuk mengubah teks menjadi suara `.wav`.

* **Antarmuka Web Interaktif**
  * Frontend menggunakan `Gradio` untuk demo dan pengujian langsung dari browser.

---

## Demo Project
## Demo Video

[![Lihat Demo](https://img.youtube.com/vi/tgZr9qRMf9k/0.jpg)](https://youtu.be/tgZr9qRMf9k)  
*Klik thumbnail di atas untuk menonton demo video.*

## Prasyarat

* Python >= 3.9
* `git` untuk meng-clone repository
* API Key Google Gemini (simpan di file `.env`)
* Model `whisper.cpp` (direpo `app/whisper.cpp`)
* Model Coqui TTS (direpo `app/coqui_utils`)

---

## Instalasi dan Setup

1. **Clone Repository**

   ```bash
   git clone https://github.com/prytarosela/2208107010046_PrytaRosela_UAS_NLP.git
   cd 2208107010046_PrytaRosela_UAS_NLP
   ```

2. **Buat Virtual Environment & Install Dependensi**

   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/macOS
   venv\\Scripts\\activate      # Windows PowerShell
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Konfigurasi API Key**

   * Buat file `.env` di root project:

     ```env
     GEMINI_API_KEY=your_api_key_here
     ```

4. **Unduh Model STT & TTS**

   * Pastikan folder `app/whisper.cpp` berisi seluruh file model Whisper.
   * Pastikan folder `app/coqui_utils` berisi model dan konfigurasi Coqui TTS.

---

## Cara Menjalankan

1. **Backend (FastAPI)**

   ```bash
   cd app
   uvicorn main:app --reload
   ```

   * API endpoint STT, LLM, dan TTS tersedia di `http://localhost:8000`.

2. **Frontend (Gradio)**

   ```bash
   cd gradio_app
   python app.py
   ```

   * Buka `http://localhost:7860` di browser.

---

## Struktur Proyek

```
2208107010046_PrytaRosela_UAS_NLP/
│
├── app/                   # Backend FastAPI & integrasi model
│   ├── main.py            # Endpoint STT, Gemini, TTS
│   ├── stt.py             # Modul transkripsi suara (whisper.cpp)
│   ├── llm.py             # Modul pemanggilan Google Gemini API
│   ├── tts.py             # Modul Coqui TTS
│   ├── whisper.cpp/       # Source whisper.cpp & model
│   └── coqui_utils/       # Model dan konfigurasi Coqui TTS
│
├── gradio_app/            # Frontend demo Gradio
│   └── app.py             # Interface Gradio
│
├── .env                   # Konfigurasi API key (gitignored)
├── requirements.txt       # Daftar dependensi Python
└── README.md              # Dokumentasi proyek
```

---

## Lisensi

Proyek ini dilisensikan di bawah lisensi MIT. Lihat file `LICENSE` untuk detail.

---

> Dibuat oleh Pryta Rosela — 2025
