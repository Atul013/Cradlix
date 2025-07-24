# Cradlix – Intelligent Baby Cry Detection & Logging System

Smart, affordable, and real-time baby monitoring—empowering caregivers with peace of mind.

---

## 🧩 Problem Statement

Traditional baby monitors lack accurate cry detection and context awareness, often leading to missed alerts or false alarms. This project addresses the challenge of reliably detecting a baby's cries, notifying caregivers promptly, reducing their anxiety, and ultimately improving infant well-being.

---

## 🚀 Solution / Innovation

**Cradlix** is a smart baby monitoring system that:
- Detects and processes baby cries in real time using high-precision audio analysis.
- Prompts caregivers via OLED display and records the reason for each cry using a capacitive touch interface.
- Logs all cry events locally and pushes annotated data to Firebase for remote monitoring and later analysis.
- Modular and ready for future machine learning integration to recognize different types of cries.

---

## 📝 Key Features / Innovations

- **Real-Time Cry Detection:** High-fidelity MEMS microphone and on-board processing minimize false alarms.
- **Wi-Fi Alerts & Cloud Sync:** Instant notifications to caregivers and reliable data backup.
- **Visual Status Indicators:** OLED display ensures clear prompts and status updates.
- **User Annotation:** 4-key touch sensor allows caregivers to specify cry reason.
- **Future-Ready:** Easily upgradeable for AI-driven cry classification and expanded IOT/smart home integration.

---

## 🎯 Impact & Benefits

- **Increases infant safety** with fast, accurate alerts for caregiver response.
- **Reduces parental stress** via reliable cry detection and fewer false alarms.
- **Improves sleep quality** for both infants and caregivers.
- **Empowers multitasking** through wireless, remote-enabled notifications.
- **Affordable and accessible**—open for further development and broad adoption.

---

## 🛠️ Technology Stack / Tools Used

- **ESP32** (core microcontroller)
- **INMP441** MEMS High Precision Omnidirectional Microphone (I2S interface)
- **TTP224** 4-Channel Capacitive Touch Sensor Module
- **Adafruit SSD1306** OLED Display
- **SD Card Module** (local logging)
- **Firebase** (cloud database/remote monitoring platform)

---

## 🔄 Approach / Methodology

- The ESP32 processes audio in real time, detecting cries via the INMP441 MEMS microphone.
- On cry detection, the OLED display prompts the caregiver to select a cry reason using the touch sensor.
- Each event (with cry reason and timestamp) is logged on the SD card and uploaded to Firebase.
- Modular design and cloud logging enable future features, analytics, and machine learning enhancements.

---

## ✅ Feasibility

- All components are affordable, widely available, and easy to integrate.
- Open-source libraries simplify both hardware and software development.
- Suitable for basic prototyping; the design is modular for future expansion.

---

## ⚡ Challenges & Workarounds

- **Cry detection accuracy:** Use noise filtering and adjustable sensitivity.
- **Reliable real-time sync:** Buffer data locally and auto-sync to Firebase as needed.
- **User data labeling:** Clear, simple prompts on OLED for consistent caregiver input.
- **Power efficiency:** Use ESP32 power-saving modes and efficient code.
- **Maintainability:** Enable over-the-air updates for smooth upgrades and fixes.

---

## 🔮 Future Scope

- Integrate **machine learning** for automatic cry-type classification.
- Develop a mobile/web dashboard for real-time analytics and insights.
- Expand features with additional sensors (e.g., temperature, humidity).
- Optimize power and enable remote firmware updates.
- Integrate with IoT and smart home devices for full ecosystem compatibility.
- Foster open-source collaboration and innovation.

---

## 👥 Team

**Team Name:** ABX & Co.  
**Leader:** Amal Babu / CSE(AI) / 3rd Year  
**Team Member 1:** Atul Biju / CSE(AI) / 3rd Year  
**Team Member 2:** aaa / CSE(AI) / 3rd Year  
**Institution:** Adi Shankara Institute of Engineering and Technology

**[GitHub Repository](https://github.com/Atul013/Cradlix)**

---

*For suggestions, contributions, or further development, please open an issue or submit a pull request!*
