# Face-for-relax
โปรแกรมนี้เป็นส่วนหนึ่งของ Project วิชา PSIT (Problem Solving in Information Technology) ซึ่งจัดทำขึ้นเพื่อแก้ปัญหาในชีวิตประจำวัน สำหรับปัญหาที่กลุ่มของพวกเราได้นำมาแก้ไขก็คือ ปัญหาด้านสุขภาพจากการนั่งทำงานหน้าคอมพิวเตอร์เป็นเวลานาน ซึ่งวิธีการที่เราใช้แก้ปัญหาคือ การนับเวลาการใช้งานคอมพิวเตอร์ด้วยการตรวจจับใบหน้า ขณะที่โปรแกรมตรวจพบใบหน้าก็จะทำการนับเวลาไปเรื่อยๆ และจะแจ้งเตือนทางหน้าจอให้ผู้ใช้งานได้ทราบ

### Built with
- Python 3.7.x
- OpenCV
- Pillow
- Tkinter
- pygame

### Installing
- Python 3.7.x

	> https://www.python.org/downloads/

	You must tick the checkbox "Add Python 3.7 to PATH" in Setup

Below is a command line that you have to paste in Command prompt.
- OpenCV
	> pip install opencv-python

- Pillow
	> pip install Pillow

- pygame
	> pip install pygame

### Instruction
1. เปิดไฟล์ project.py
2. ตั้งค่าเวลาในหน่วย ชั่วโมง, นาที และ วินาที ตามลำดับ
3. กดปุ่ม Start จะทำให้โปรแกรมเริ่มทำการจับใบหน้าและเมื่อพบใบหน้าจะทำการนับเวลา
4. หากคุณกด Start แล้วต้องการยกเลิกการใช้งานก่อนที่เวลาจะถึงเวลาที่กำหนดไว้ สามารถกดปุ่ม Reset เพื่อยกเลิกการตรวจจับใบหน้าและนับเวลาได้
5. เมื่อนับเวลาถึงเวลาที่ตั้งไว้ จะแสดง Popup

	5.1 กด Yes หากคุณจะไม่ใช้งานคอมพิวเตอร์และไปพักผ่อน โปรแกรมจะหยุดทำงาน

	5.2 กด No หากคุณต้องการใช้งานคอมพิวเตอร์ต่อสักพัก โปรแกรมจะเริ่มนับเวลาใหม่อีกครั้ง

    <img src="image_instruction\instruction.png" width="1280">

### References
- [Face detection with OpenCV Python](https://www.youtube.com/watch?v=kVv2oez_70M&list=PLEE74DyIkwEnj1NEawe-0rRsjWpZgU8hi&index=8)
- [Tkinter Tutorial 1](https://www.youtube.com/watch?v=bWkwHpY7F_4&list=PLEE74DyIkwEl9Mr7GuItlE2hsAW5suKwE)
- [Tkinter Tutorial 2](https://www.youtube.com/watch?v=O8cvJZgbEA0&list=PLoTScYm9O0GFB1Y3cCmb9aPD5xRB1T11y)

### Contributors

| รหัสนักศึกษา | ชื่อ - นามสกุล | GitHub |
| ---------- | ------------ | ---------- |
| 62070021 | นายคณาสิน อมรกิตติสาร | [62070021](https://github.com/62070021) |
| 62070090 | นายธัชพนธ์ ศรีอากาศไกรแสง | [zaxscdqwer7](https://github.com/zaxscdqwer7) |
| 62070113 | นายประธาน นาเวียง | [PrathanNawiang62070113](https://github.com/PrathanNawiang62070113) |
| 62070147 | นายภัทรพล เงารัตนพันธิกุล | [it62070147](https://github.com/it62070147) |
| 62070154 | นายภูวนัตถ์ จันทร์มี | [pwn154](https://github.com/pwn154) |