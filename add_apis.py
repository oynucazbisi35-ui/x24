import codecs

new_apis = '''
    #api.mock-service.example.com
    def MockService(self):
        try:
            url = "https://api.mock-service.example.com/v1/auth/register"
            headers = {"User-Agent": "Mozilla/5.0"}
            json={"phone": self.phone}
            r = requests.post(url, headers=headers, json=json, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Basarili! {self.phone} --> mock-service.example.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Basarisiz! {self.phone} --> mock-service.example.com")

    #otp.fictional-brand.net
    def FictionalBrand(self):
        try:
            url = "https://otp.fictional-brand.net/send"
            headers = {"User-Agent": "Mozilla/5.0"}
            data={"msisdn": f"90{self.phone}"}
            r = requests.post(url, headers=headers, data=data, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Basarili! {self.phone} --> fictional-brand.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Basarisiz! {self.phone} --> fictional-brand.net")

    #auth.generic-ecommerce.org
    def GenericEcommerce(self):
        try:
            url = f"https://auth.generic-ecommerce.org/login?phone={self.phone}"
            headers = {"User-Agent": "Mozilla/5.0"}
            r = requests.get(url, headers=headers, timeout=6)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Basarili! {self.phone} --> generic-ecommerce.org")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Basarisiz! {self.phone} --> generic-ecommerce.org")
'''

with codecs.open('sms.py', 'a', 'utf-8') as f:
    f.write(new_apis)
