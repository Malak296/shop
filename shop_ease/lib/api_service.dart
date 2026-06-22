import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {

  // =========================
  // 🔵 REGISTER
  // =========================
  Future<void> registerUser() async {
    print("🔥 REGISTER CLICKED");

    try {
      final response = await http.post(
        Uri.parse('http://127.0.0.1:8000/api/register/'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          "username": "test",
          "password": "123456"
        }),
      );

      print("✅ REGISTER STATUS: ${response.statusCode}");
      print("📦 REGISTER BODY: ${response.body}");

    } catch (e) {
      print("❌ REGISTER ERROR: $e");
    }
  }

  // =========================
  // 🟢 LOGIN
  // =========================
  Future<void> loginUser(String username, String password) async {
    print("🔥 LOGIN CLICKED");

    try {
      final response = await http.post(
        Uri.parse('http://127.0.0.1:8000/api/login/'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          "username": username,
          "password": password
        }),
      );

      print("✅ LOGIN STATUS: ${response.statusCode}");
      print("📦 LOGIN BODY: ${response.body}");

    } catch (e) {
      print("❌ LOGIN ERROR: $e");
    }
  }
}