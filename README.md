# Micro:bit Project – Computer Architecture  
**Team:**  
Het Chavadia (BT2024052) – [Het.Chavadia@iiitb.ac.in](mailto:Het.Chavadia@iiitb.ac.in)  
P. Pranav Sai (BT2024099) – [Pranav.Sai@iiitb.ac.in](mailto:Pranav.Sai@iiitb.ac.in)  
Srikar Vellanki (BT2024081) – [Srikar.Vellanki@iiitb.ac.in](mailto:Srikar.Vellanki@iiitb.ac.in)  
Nethi Vishwa Pradyumna (BT2024157) – [Pradyumna.Nethi@iiitb.ac.in](mailto:Pradyumna.Nethi@iiitb.ac.in)  
B Haneesh Reddy (BT2024126) – [Haneesh.Bandi@iiitb.ac.in](mailto:Haneesh.Bandi@iiitb.ac.in)  
Kommireddy Dhanush Chennakesava Reddy (BT2024169) – [Dhanush.Kommireddy@iiitb.ac.in](mailto:Dhanush.Kommireddy@iiitb.ac.in)  
Chovatiya Laksh Vipulbhai (BT2024056) – [Laksh.Chovatiya@iiitb.ac.in](mailto:Laksh.Chovatiya@iiitb.ac.in)

---

## 🔗 GitHub Repository
[https://github.com/Het2239/Microbit-Project.git](https://github.com/Het2239/Microbit-Project.git)

---

## 📁 Project Overview

Our goal was to explore the full capabilities of the BBC Micro:bit using both **MicroPython** and **ARM Assembly**. We initially aimed to integrate all components into one program, but hardware constraints led us to split the functionality into independent modules. Each module demonstrates different computer architecture concepts and embedded programming practices.

---

## 🧠 Projects Summary

### 1. **LED Light Show (ARM Assembly)**  
**Language:** ARM Thumb Assembly  
**Hardware Used:** GPIO, LED Matrix  

**Objective:**  
Animate the 5×5 LED matrix using predefined patterns by directly manipulating GPIO through low-level ARM assembly code.

**Highlights:**  
- Manual GPIO setup and pin writing  
- Row multiplexing for stable LED visuals  
- Bitwise pattern manipulation and memory access  
- Looping 8 unique frame animations  

**Execution Steps:**  
1. Install the ARM toolchain  
2. Open `workfolder` in VS Code  
3. Press `Ctrl+Shift+P` → `comp2300: Build`  
4. Then `comp2300: Upload`  

**Source File:** `src/main.S`  
**Demo:** [Watch on YouTube](https://youtu.be/O_ggjn6FVf8?si=NjNnJ7hOHfLh24P5)

---

### 2. **Compass Direction Display**  
**Language:** MicroPython  
**Hardware Used:** Magnetometer, Accelerometer, LED Matrix  

**Objective:**  
Display compass directions (N, E, SW, etc.) on the LED matrix, using heading and pitch data to ensure accuracy.

**Highlights:**  
- Uses `compass.heading()` for direction  
- Ensures Micro:bit is flat using accelerometer pitch  
- Displays one of 8 cardinal directions  
- Blank display if tilted beyond threshold  

**Concepts Demonstrated:**  
- Sensor filtering  
- Trigonometric angle checks  
- Condition-based matrix display  

**Demo:** [Watch on YouTube](https://youtu.be/ko8QysBHSBw?feature=shared)

---

### 3. **Music Player with Visual Feedback**  
**Language:** MicroPython  
**Hardware Used:** Buttons A/B, LED Matrix, Built-in Speaker  

**Objective:**  
Play 5 predefined songs with matching visual effects on the LED matrix.

**Highlights:**  
- Press **B** to switch songs, **A** to play  
- Song title scrolls before playback  
- Animated visuals using random brightness  
- Ends with a smiley face after playback  

**Concepts Demonstrated:**  
- Event-driven button handling  
- Audio-visual synchronization  
- Random number usage for dynamic effects  
- LED matrix updates in sync with sound  

**Demo:** [Watch on YouTube](https://youtu.be/Eqfr77lXZjs?feature=shared)

---

### 4. **Fruit Shoot – Reflex-Based LED Game**  
**Language:** MicroPython  
**Hardware Used:** Buttons A/B, LED Matrix, Built-in Speaker  

**Objective:**  
Shoot falling fruits by aligning the bullet row with the falling fruit.

**Gameplay:**  
- **Button A**: Fire bullet  
- **Button B**: Change active row  
- Fruits fall vertically, bullets fire horizontally  
- Score increases on hits; 5 lives available  

**Levels:**  
- 3 levels with increasing difficulty  
- Level 3 includes fruit lateral movement  

**Feedback:**  
- Sounds for shooting/hit/miss  
- Heart icons for lives  
- Happy/sad face for win/loss  

**Concepts Demonstrated:**  
- Polling-based input  
- Real-time collision detection  
- Game state tracking  
- Pseudo-interrupts using `running_time()`  

**Demo:** [Watch on YouTube](https://youtu.be/2XyopDEJJwA?feature=shared)

---

### 5. **DodgeBolt – Turn-Based Wireless Multiplayer Game**  
**Language:** MicroPython  
**Hardware Used:** Radio, Buttons A/B, LED Matrix  

**Objective:**  
Two-player wireless game where players switch roles between **Shooter** and **Dodger**.

**Controls:**  
- Shooter: Press **A+B** to fire  
- Dodger: Press **A** to move left, **B** to move right  
- Roles switch every 2 shots  
- Dodger’s movement space shrinks over time  

**Key Challenges Solved:**  
- Unbuffered `radio.receive()` → mitigated using frequent polling  
- Synchronized state management using custom FSM  
- Combined button detection (A+B) via input timing  

**Concepts Demonstrated:**  
- Real-time wireless communication  
- Finite state machine for roles and turns  
- Dynamic visual rendering on LED matrix  
- Fault tolerance and recovery  

**Demo:** [Watch on YouTube](https://youtu.be/t6WU4v4seMU?feature=shared)

---

## 🧠 Computer Architecture Concepts Applied

| Category                 | Techniques Used                                       |
|--------------------------|--------------------------------------------------------|
| GPIO & Low-level Control | ARM Assembly, direct pin toggling                     |
| Sensor Integration       | Accelerometer, Magnetometer filtering                 |
| Event-driven I/O         | Button polling, debounce logic                        |
| Real-Time Systems        | Timing loops, game loop, `running_time()` usage       |
| State Management         | FSMs, score/lives tracking                            |
| Communication Protocols  | MicroPython radio, role-based message exchange        |
| Display Logic            | LED matrix row-column multiplexing                    |
| Sound Feedback           | Speaker tones tied to events                          |

---

## 📌 Conclusion

This multi-part project explores both the high-level simplicity of MicroPython and the low-level power of ARM assembly on the BBC Micro:bit. Each module showcases key aspects of embedded systems and computer architecture, from direct memory manipulation and IO timing to state-driven gameplay and wireless synchronization. Despite hardware constraints, we built meaningful, interactive applications that deepen our understanding of how computing systems interact with the physical world.

---

