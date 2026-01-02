# Network Security Lab: ARP Protocol Analysis ⚔️

A comprehensive research project demonstrating the vulnerabilities of the ARP protocol and how to detect them. This repository contains both an **Attack PoC** and a **Defense Detection Tool**.

## 📂 Project Structure
- **Red Team (`spoofer.py`):** A proof-of-concept script that demonstrates ARP Cache Poisoning by masquerading as the gateway. Includes graceful exit and network restoration logic.
- **Blue Team (`watchdog.py`):** A Network Intrusion Detection System (NIDS) that monitors traffic for MAC address anomalies and alerts on potential spoofing attempts.

## 🧪 The Experiment
The goal of this project is to simulate a local network attack in a controlled environment to understand:
1.  **The Attack Vector:** How lack of authentication in ARP allows identity spoofing.
2.  **The Defense:** How to programmatically detect mapping changes in real-time.

## ⚠️ Disclaimer
**This software is for educational purposes only.** It is designed to be used in a controlled lab environment (e.g., your own home network or a virtual cyber range). Unauthorized ARP spoofing on public or corporate networks is illegal.

## 🚀 Usage

### Step 1: Configure
Edit `config.yaml` with your lab IPs.

### Step 2: Start Defense (Terminal 1)
```bash
sudo python3 spoofer.py
