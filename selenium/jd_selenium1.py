from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# 初始化驱动
driver = webdriver.Safari()
driver.maximize_window()

try:
    print("正在打开京东首页...")
    driver.get("https://www.jd.com/")
    
    # 等待页面标题包含 "京东"，确保页面基本加载
    WebDriverWait(driver, 10).until(
        EC.title_contains("京东")
    )
    print(f"页面已加载，标题: {driver.title}")

    # 尝试处理可能的弹窗干扰 (例如登录弹窗或广告)
    # 注意：选择器可能需要根据实际页面情况调整，这里尝试常见的关闭按钮类名
    try:
        close_buttons = driver.find_elements(By.CSS_SELECTOR, ".ui-dialog-close, .close-btn, .J_close")
        for btn in close_buttons:
            if btn.is_displayed():
                btn.click()
                print("已尝试关闭弹窗")
                time.sleep(1)
    except Exception:
        pass

    # 等待搜索框存在
    print("正在查找搜索框...")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "key"))
    )
    
    # 清除默认内容
    search_box.clear()
    
    # 方法1：常规发送按键
    try:
        search_box.send_keys("手机")
        search_box.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"常规输入失败，尝试 JS 注入: {e}")
        # 方法2：如果常规方法失败，使用 JavaScript 强制赋值并触发回车
        driver.execute_script("arguments[0].value = '手机';", search_box)
        driver.execute_script("arguments[0].dispatchEvent(new KeyboardEvent('keydown', {'key': 'Enter'}));", search_box)

    print("已执行搜索，等待结果加载...")
    
    # 等待搜索结果列表出现 (京东搜索结果通常包含 class "gl-item")
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".gl-item"))
    )
    
    print("搜索成功！页面已显示结果。")
    time.sleep(5) # 停留5秒以便观察

except TimeoutException:
    print("错误：操作超时。可能是网络慢或页面结构变化。")
    # 截图调试
    driver.save_screenshot("timeout_debug.png")
    print("已保存调试截图: timeout_debug.png")
    
except Exception as e:
    print(f"发生未知错误: {type(e).__name__}: {e}")

finally:
    print("关闭浏览器...")
    driver.quit()


# (selenium) douxiaobo@192 selenium % pip3 install webdriver-manager
# Collecting webdriver-manager
#   Downloading webdriver_manager-4.1.2-py3-none-any.whl.metadata (16 kB)
# Collecting requests (from webdriver-manager)
#   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
# Collecting python-dotenv (from webdriver-manager)
#   Downloading python_dotenv-1.2.2-py3-none-any.whl.metadata (27 kB)
# Collecting packaging (from webdriver-manager)
#   Downloading packaging-26.2-py3-none-any.whl.metadata (3.5 kB)
# Collecting charset_normalizer<4,>=2 (from requests->webdriver-manager)
#   Downloading charset_normalizer-3.4.7-cp313-cp313-macosx_10_13_universal2.whl.metadata (40 kB)
# Requirement already satisfied: idna<4,>=2.5 in ./selenium/lib/python3.13/site-packages (from requests->webdriver-manager) (3.18)
# Requirement already satisfied: urllib3<3,>=1.26 in ./selenium/lib/python3.13/site-packages (from requests->webdriver-manager) (2.7.0)
# Requirement already satisfied: certifi>=2023.5.7 in ./selenium/lib/python3.13/site-packages (from requests->webdriver-manager) (2026.6.17)
# Downloading webdriver_manager-4.1.2-py3-none-any.whl (32 kB)
# Downloading packaging-26.2-py3-none-any.whl (100 kB)
# Downloading python_dotenv-1.2.2-py3-none-any.whl (22 kB)
# Downloading requests-2.34.2-py3-none-any.whl (73 kB)
# Downloading charset_normalizer-3.4.7-cp313-cp313-macosx_10_13_universal2.whl (309 kB)
# Installing collected packages: python-dotenv, packaging, charset_normalizer, requests, webdriver-manager
# Successfully installed charset_normalizer-3.4.7 packaging-26.2 python-dotenv-1.2.2 requests-2.34.2 webdriver-manager-4.1.2

# [notice] A new release of pip is available: 25.2 -> 26.1.2
# [notice] To update, run: pip install --upgrade pip
# (selenium) douxiaobo@192 selenium % python3 jd_selenium1.py       
# 正在打开京东首页...
# 页面已加载，标题: 京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！
# 正在查找搜索框...
# 错误：操作超时。可能是网络慢或页面结构变化。
# 已保存调试截图: timeout_debug.png
# 关闭浏览器...
# (selenium) douxiaobo@192 selenium % 
