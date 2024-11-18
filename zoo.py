class Zoo:
    def get_ticket_price(self, age):
        if age < 0:
            return 0  # ให้เป็น0เพราะโอกาสน้อยกว่า0ปีเป็นไปได้ยากมาก
        elif 0 <= age <= 12:
            return 50
        elif 13 <= age <= 20:
            return 100
        elif 21 <= age <= 60:
            return 150
        elif age > 60:
            return 100
        else:
            return 0 # อายุไม่อยู่ในช่วงที่กำหนด
