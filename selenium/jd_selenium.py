from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Safari()
driver.maximize_window()        # 最大化窗口，确保元素可见
driver.get("https://www.jd.com/")

# try:
#     # 显式等待：最多等待 10 秒，直到 ID 为 'key' 的元素可见
#     search_box = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "key"))
#     )
    
#     search_box.send_keys("手机")
#     search_box.send_keys(Keys.ENTER)
    
#     # 可选：等待搜索结果页面加载，例如等待某个结果元素出现
#     # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gl-item")))
    
# except Exception as e:
#     print(f"发生错误: {e}")
# finally:
#     # 为了观察结果，可以暂停几秒再关闭，或者直接关闭
#     import time
#     time.sleep(5) 
#     driver.quit()  # 推荐使用 quit() 而不是 close()，它会关闭所有窗口并结束驱动进程


# (selenium) douxiaobo@192 selenium % python3 jd_selenium.py
# 发生错误: Message: 

# (selenium) douxiaobo@192 selenium % 



try:
    # 1. 等待页面基本加载
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "key"))
    )
    
    # 2. 尝试处理可能的弹窗干扰 (可选，根据实际页面情况调整)
    # 如果有关闭按钮，可以尝试点击关闭。例如：
    # try:
    #     close_btn = driver.find_element(By.CSS_SELECTOR, ".ui-dialog-close")
    #     close_btn.click()
    # except:
    #     pass

    # 3. 找到搜索框
    search_box = driver.find_element(By.ID, "key")
    
    # 4. 清除可能存在的默认文本并输入
    search_box.clear()
    search_box.send_keys("手机")
    
    # 5. 发送回车键
    search_box.send_keys(Keys.ENTER)
    
    # 6. 等待搜索结果加载 (验证是否成功)
    # 这里等待搜索结果列表中的第一个商品出现
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".gl-item"))
    )
    print("搜索成功，页面已加载结果。")
    time.sleep(5) # 观察结果

except TimeoutException:
    print("错误：等待元素超时。请检查网络连接或页面结构是否变化。")
except Exception as e:
    print(f"发生未知错误: {type(e).__name__}: {e}")
finally:
    driver.quit()



# (selenium) douxiaobo@192 selenium % python3 jd_selenium.py
# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/selenium/jd_selenium.py", line 42, in <module>
#     WebDriverWait(driver, 10).until(
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
#         EC.presence_of_element_located((By.ID, "key"))
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#     )
#     ^
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/selenium/selenium/lib/python3.13/site-packages/selenium/webdriver/support/wait.py", line 121, in until
#     raise TimeoutException(message, screen, stacktrace)
# selenium.common.exceptions.TimeoutException: Message: 


# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/selenium/jd_selenium.py", line 72, in <module>
#     except TimeoutException:
#            ^^^^^^^^^^^^^^^^
# NameError: name 'TimeoutException' is not defined
# (selenium) douxiaobo@192 selenium % 




# douxiaobo@192 selenium % code .
# douxiaobo@192 selenium % python3 -m venv selenium
# douxiaobo@192 selenium % source selenium/bin/activate
# (selenium) douxiaobo@192 selenium % pip3 install selenium
# Collecting selenium
#   Downloading selenium-4.45.0-py3-none-any.whl.metadata (7.4 kB)
# Collecting certifi>=2026.2.25 (from selenium)
#   Downloading certifi-2026.6.17-py3-none-any.whl.metadata (2.5 kB)
# Collecting trio<1.0,>=0.31.0 (from selenium)
#   Downloading trio-0.33.0-py3-none-any.whl.metadata (8.5 kB)
# Collecting trio-websocket<1.0,>=0.12.2 (from selenium)
#   Downloading trio_websocket-0.12.2-py3-none-any.whl.metadata (5.1 kB)
# Collecting typing_extensions<5.0,>=4.15.0 (from selenium)
#   Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
# Collecting urllib3<3.0,>=2.6.3 (from urllib3[socks]<3.0,>=2.6.3->selenium)
#   Downloading urllib3-2.7.0-py3-none-any.whl.metadata (6.9 kB)
# Collecting websocket-client<2.0,>=1.8.0 (from selenium)
#   Downloading websocket_client-1.9.0-py3-none-any.whl.metadata (8.3 kB)
# Collecting attrs>=23.2.0 (from trio<1.0,>=0.31.0->selenium)
#   Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
# Collecting sortedcontainers (from trio<1.0,>=0.31.0->selenium)
#   Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl.metadata (10 kB)
# Collecting idna (from trio<1.0,>=0.31.0->selenium)
#   Downloading idna-3.18-py3-none-any.whl.metadata (6.1 kB)
# Collecting outcome (from trio<1.0,>=0.31.0->selenium)
#   Downloading outcome-1.3.0.post0-py2.py3-none-any.whl.metadata (2.6 kB)
# Collecting sniffio>=1.3.0 (from trio<1.0,>=0.31.0->selenium)
#   Using cached sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
# Collecting wsproto>=0.14 (from trio-websocket<1.0,>=0.12.2->selenium)
#   Downloading wsproto-1.3.2-py3-none-any.whl.metadata (5.2 kB)
# Collecting pysocks!=1.5.7,<2.0,>=1.5.6 (from urllib3[socks]<3.0,>=2.6.3->selenium)
#   Downloading PySocks-1.7.1-py3-none-any.whl.metadata (13 kB)
# Collecting h11<1,>=0.16.0 (from wsproto>=0.14->trio-websocket<1.0,>=0.12.2->selenium)
#   Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
# Downloading selenium-4.45.0-py3-none-any.whl (9.5 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.5/9.5 MB 24.6 kB/s  0:05:06
# Downloading trio-0.33.0-py3-none-any.whl (510 kB)
# Downloading trio_websocket-0.12.2-py3-none-any.whl (21 kB)
# Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
# Downloading urllib3-2.7.0-py3-none-any.whl (131 kB)
# Downloading PySocks-1.7.1-py3-none-any.whl (16 kB)
# Downloading websocket_client-1.9.0-py3-none-any.whl (82 kB)
# Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
# Downloading certifi-2026.6.17-py3-none-any.whl (133 kB)
# Downloading outcome-1.3.0.post0-py2.py3-none-any.whl (10 kB)
# Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
# Downloading wsproto-1.3.2-py3-none-any.whl (24 kB)
# Using cached h11-0.16.0-py3-none-any.whl (37 kB)
# Downloading idna-3.18-py3-none-any.whl (65 kB)
# Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl (29 kB)
# Installing collected packages: sortedcontainers, websocket-client, urllib3, typing_extensions, sniffio, pysocks, idna, h11, certifi, attrs, wsproto, outcome, trio, trio-websocket, selenium
# Successfully installed attrs-26.1.0 certifi-2026.6.17 h11-0.16.0 idna-3.18 outcome-1.3.0.post0 pysocks-1.7.1 selenium-4.45.0 sniffio-1.3.1 sortedcontainers-2.4.0 trio-0.33.0 trio-websocket-0.12.2 typing_extensions-4.15.0 urllib3-2.7.0 websocket-client-1.9.0 wsproto-1.3.2

# [notice] A new release of pip is available: 25.2 -> 26.1.2
# [notice] To update, run: pip install --upgrade pip
# (selenium) douxiaobo@192 selenium % 





# 这个错误是因为 macOS 上的 Safari 浏览器默认禁止了远程自动化控制。你需要手动开启 Safari 的开发者选项中的“允许远程自动化”功能。

# 请按照以下步骤操作：

# 打开 Safari 浏览器。
# 点击菜单栏左上角的 Safari 浏览器 > 设置... (或偏好设置)。
# 点击顶部的 高级 标签页。
# 勾选最下方的 在菜单栏中显示“开发”菜单 (Show Develop menu in menu bar)。
# 关闭设置窗口，现在菜单栏中会出现一个 开发 (Develop) 菜单。
# 点击 开发 菜单，找到并勾选 允许远程自动化 (Allow Remote Automation)。
# 完成上述设置后，重新运行你的 Python 脚本 python3 jd_selenium.py 即可正常启动 Safari 驱动。