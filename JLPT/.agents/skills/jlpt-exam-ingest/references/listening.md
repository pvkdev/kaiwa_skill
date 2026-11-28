# Một audio tổng cho mỗi đề

Dùng [skill jlpt-listening](../../jlpt-listening/SKILL.md) để đọc mốc nguồn, khôi phục script với Groq khi thiếu, ráp timeline và bàn giao đúng ID cho importer.

Ví dụ đối chiếu biên chung có trong nguồn N2 tháng 12/2018. HTML nghe SHA-256 `67154e0a830edf6663101d503a973ed182cd1f3a840489f5f431df139741d25f` có player trong `#q-30` ghi `data-start="2204.25"` và `data-end="2338.12"`. Câu 29 và 30 dùng chung khoảng 2.204.250–2.338.120 ms. Muốn gắn biên riêng cho từng câu cần đối chiếu tín hiệu trên master.
