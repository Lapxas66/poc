# 百易云资产SQL注入检测工具

## 免责声明
**本工具仅供授权的安全测试和教育目的使用。未经授权使用此工具攻击他人系统是违法的。使用者需自行承担所有法律责任。**

## 功能说明
- 检测百易云资产系统的SQL注入漏洞
- 支持单个URL和批量检测
- 基于报错注入（XPATH报错）原理

## 安装依赖
pip install -r requirements.txt

## 使用方法

### 单个URL检测
python sql_scanner.py -u http://example.com

### 批量检测
python sql_scanner.py -f urls.txt

## 参数说明
-u 指定单个URL
-f 指定URL列表文件

## 依赖库
requests
urllib3

## 输出结果
检测到漏洞的URL会自动保存到 result.txt 文件中。
