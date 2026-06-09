import pytest
from Crypto.Cipher import AES
import base64

from aes_demo import encrypt, decrypt


class TestEncrypt:
    def test_encrypt_normal_text(self):
        """测试正常文本加密"""
        result = encrypt("hello world")
        assert isinstance(result, str)
        assert len(result) > 0
        # 验证可以base64解码
        decoded = base64.b64decode(result.encode('utf-8'))
        assert len(decoded) % 16 == 0

    def test_encrypt_empty_string(self):
        """测试空字符串加密"""
        result = encrypt("")
        assert isinstance(result, str)
        assert len(result) > 0
        decoded = base64.b64decode(result.encode('utf-8'))
        # 空字符串需要16字节padding
        assert len(decoded) == 16

    def test_encrypt_exact_16_bytes(self):
        """测试正好16字节的文本加密"""
        text = "1234567890123456"
        result = encrypt(text)
        assert isinstance(result, str)
        decoded = base64.b64decode(result.encode('utf-8'))
        assert len(decoded) == 16

    def test_encrypt_17_bytes(self):
        """测试17字节文本加密（跨16字节边界）"""
        text = "12345678901234567"
        result = encrypt(text)
        assert isinstance(result, str)
        decoded = base64.b64decode(result.encode('utf-8'))
        assert len(decoded) == 32

    def test_encrypt_unicode_text(self):
        """测试Unicode文本加密"""
        text = "你好世界"
        result = encrypt(text)
        assert isinstance(result, str)
        assert len(result) > 0
        decoded = base64.b64decode(result.encode('utf-8'))
        assert len(decoded) % 16 == 0

    def test_encrypt_english_text(self):
        """测试纯英文文本加密"""
        text = "Hello, World! This is a test."
        result = encrypt(text)
        assert isinstance(result, str)
        decoded = base64.b64decode(result.encode('utf-8'))
        assert len(decoded) % 16 == 0

    def test_encrypt_mixed_content(self):
        """测试混合内容加密"""
        text = "Test123!@#$%^&*()"
        result = encrypt(text)
        assert isinstance(result, str)
        decoded = base64.b64decode(result.encode('utf-8'))
        assert len(decoded) % 16 == 0


class TestDecrypt:
    def test_decrypt_normal_text(self):
        """测试正常文本解密"""
        original = "hello world"
        encrypted = encrypt(original)
        result = decrypt(encrypted)
        assert result == original

    def test_decrypt_empty_string(self):
        """测试空字符串解密"""
        encrypted = encrypt("")
        result = decrypt(encrypted)
        assert result == ""

    def test_decrypt_exact_16_bytes(self):
        """测试正好16字节文本解密"""
        original = "1234567890123456"
        encrypted = encrypt(original)
        result = decrypt(encrypted)
        assert result == original

    def test_decrypt_17_bytes(self):
        """测试17字节文本解密"""
        original = "12345678901234567"
        encrypted = encrypt(original)
        result = decrypt(encrypted)
        assert result == original

    def test_decrypt_unicode_text(self):
        """测试Unicode文本解密"""
        original = "你好世界"
        encrypted = encrypt(original)
        result = decrypt(encrypted)
        assert result == original

    def test_decrypt_english_text(self):
        """测试英文文本解密"""
        original = "Hello, World! This is a test."
        encrypted = encrypt(original)
        result = decrypt(encrypted)
        assert result == original

    def test_decrypt_mixed_content(self):
        """测试混合内容解密"""
        original = "Test123!@#$%^&*()"
        encrypted = encrypt(original)
        result = decrypt(encrypted)
        assert result == original


class TestEncryptDecryptRoundTrip:
    """测试加密解密往返（加解密互逆性）"""

    def test_roundtrip_various_lengths(self):
        """测试不同长度的往返加解密"""
        test_cases = [
            "",
            "a",
            "ab",
            "abc",
            "abcd",
            "abcde",
            "abcdef",
            "abcdefg",
            "abcdefgh",
            "abcdefghi",
            "abcdefghij",
            "abcdefghijk",
            "abcdefghijkl",
            "abcdefghijklm",
            "abcdefghijklmn",
            "abcdefghijklmno",
            "a" * 100,
            "测试中文文本",
        ]
        for original in test_cases:
            encrypted = encrypt(original)
            decrypted = decrypt(encrypted)
            assert decrypted == original, f"Failed for: {original}"

    def test_roundtrip_special_characters(self):
        """测试特殊字符的往返加解密"""
        test_cases = [
            "!@#$%^&*()",
            "   ",
            "\n\t\r",
            "中文!@#$测试",
        ]
        for original in test_cases:
            encrypted = encrypt(original)
            decrypted = decrypt(encrypted)
            assert decrypted == original


class TestDecryptInvalidInput:
    """测试无效输入解密"""

    def test_decrypt_invalid_base64(self):
        """测试无效Base64输入解密"""
        with pytest.raises(Exception):
            decrypt("not_valid_base64!!!")

    def test_decrypt_empty_string(self):
        """测试空字符串解密"""
        with pytest.raises(Exception):
            decrypt("")

    def test_decrypt_too_short_data(self):
        """测试数据过短解密"""
        # AES ECB 块大小为16字节
        with pytest.raises(Exception):
            decrypt(base64.b64encode(b"short").decode('utf-8'))