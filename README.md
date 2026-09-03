<div align="center">

![Animated header](https://capsule-render.vercel.app/api?type=waving&amp;color=0:ef4444,50:22c55e,100:3b82f6&amp;height=210&amp;section=header&amp;text=Kitchen%20Quantity&amp;fontSize=48&amp;fontColor=ffffff&amp;animation=fadeIn&amp;fontAlignY=36&amp;desc=Test-Driven%20Development%20with%20Python&amp;descAlignY=57)

[![Typing introduction](https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=700&amp;size=24&amp;pause=800&amp;color=22C55E&amp;center=true&amp;vCenter=true&amp;repeat=true&amp;width=760&amp;lines=%F0%9F%94%B4+RED+%E2%80%94+Write+a+failing+test;%F0%9F%9F%A2+GREEN+%E2%80%94+Make+the+test+pass;%F0%9F%94%B5+REFACTOR+%E2%80%94+Improve+with+confidence;%E2%9C%85+8+tests+passing)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white)
![pytest](https://img.shields.io/badge/pytest-8%20passing-0A9EDC?style=for-the-badge&amp;logo=pytest&amp;logoColor=white)
![TDD](https://img.shields.io/badge/workflow-RED%20%E2%86%92%20GREEN%20%E2%86%92%20REFACTOR-22C55E?style=for-the-badge)

</div>

# ITDS362: Test-Driven Development

แบบฝึกหัด Kitchen Quantity พัฒนาด้วยวงจร **Red–Green–Refactor** โดยมีประวัติ commit แยกแต่ละขั้นไว้เป็นหลักฐาน

## Red–Green–Refactor คืออะไร

<div align="center">

![วงจร TDD แบบเคลื่อนไหว](assets/tdd-cycle.svg)

</div>

- **RED:** เขียนเทสต์ของพฤติกรรมใหม่ก่อน แล้วรันเพื่อยืนยันว่าเทสต์ล้มเหลวจริง
- **GREEN:** เขียนโค้ดให้น้อยที่สุดเพื่อทำให้เทสต์ใหม่และเทสต์เดิมทั้งหมดผ่าน
- **REFACTOR:** ลดความซ้ำซ้อนและปรับโครงสร้าง โดยรักษาให้เทสต์ทั้งหมดยังผ่าน

ตัวอย่างจากงานนี้คือ commit `A2 RED` เพิ่มกรณี `200 × 2 = 400` ซึ่งทำให้โค้ดที่คืนค่า 600 ตลอดล้มเหลว จากนั้น commit `A2 GREEN` จึงเปลี่ยนเป็นการคำนวณ `amount * multiplier` วิธีนี้คือ **Triangulate**

## พฤติกรรมที่พัฒนา

- คูณปริมาณโดยไม่แก้ไขอ็อบเจ็กต์เดิม
- เปรียบเทียบปริมาณด้วยจำนวนและหน่วย
- บวกปริมาณหน่วยเดียวกันและต่างหน่วย
- กำหนดอัตราแปลงหน่วยผ่าน `Converter`
- คูณนิพจน์ผลบวก เช่น `(200 g + 1 oz) × 2`

การออกแบบใช้ `Quantity` เป็น value object, `Sum` เก็บนิพจน์การบวก และ `Converter` ลดรูปผลลัพธ์ไปยังหน่วยที่ต้องการ

## วิธีรันเทสต์

```bash
source .venv/bin/activate
pytest -q
```

ผลลัพธ์ปัจจุบัน: `8 passed`

```text
........  [100%]
8 passed
```

รายละเอียดการทบทวนกระบวนการอยู่ใน [REFLECTION.md](REFLECTION.md)

<div align="center">

![Animated footer](https://capsule-render.vercel.app/api?type=waving&amp;color=0:3b82f6,50:22c55e,100:ef4444&amp;height=120&amp;section=footer&amp;animation=twinkling)

</div>
