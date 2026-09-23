# Gregory-Pad
# 🚀 Custom 4x4 Mechanical Macro Pad

Welcome to my custom-engineered 4x4 macro pad project, designed as part of the **Hack Club Stardance/Hackpad** mission! This device features an ortholinear key matrix, advanced anti-ghosting rotary encoder input, and a high-resolution OLED status display screen.

---

## 🛠️ Hardware Specifications

- **Microcontroller:** Seeed Studio XIAO 
- **Key Layout:** 16-key (4x4 Matrix) uniform arrangement (custom `19.69 mm` spacing)
- **Key Switches:**  Gateron KS-3X1 Milky Yellow Pro Linear Switches with Kailh Hotswap Sockets
- **Accessory Cluster:** 
  - 1x Rotary Encoder Volume Dial (equipped with anti-ghosting input isolation diodes `D17` and `D18`)
  - 1x Waveshare 1.5-inch OLED Display Module (`26.86 mm` active square glass window)

---

## 📐 Enclosure Design & Architecture

The chassis is designed completely from scratch using **Onshape** using a highly rigid **Bottom-Up Sandwich Mount System**. My PCB is 110x110mm with curved edges

- **Layer Breakdown:**
  - **Top Bezel Cap:** 4.5mm thick protective frame with a flush 9mm encoder dial portal and a custom 27.5mm tolerance screen window. Totally clean top face with hidden screw anchors.
  - **Middle Spacer Walls:** 13mm thick hollow wall ring with integrated rounded internal corner fillets designed to smoothly scatter the underglow light from the RGB LED strip. Features an inline 15mm x 8.5mm side-mounted USB-C pass-through tunnel for maximum cable mold clearance.
  - **Bottom Base Plate:** 6mm thick solid floor slab featuring 4 deep mechanical counterbore screw pockets to hide the mounting hardware heads completely flush with the desk surface.
- **Tolerances:** Applied a micro-precise `0.4 mm` gap buffer across all internal pocket steps to easily absorb 3D printing plastic cooling shrinkage without component binding.

---

## 📂 Project Repository Structure

- `/KiCad/` - Contains the electrical schematic diagram sheets, netlists, trace footprints, and production Gerber fabrication zip bundles.
- `/CAD/` - Houses the 3D-printable `.STL` and `.STEP` mechanical mesh file models exported from Onshape.
- `README.md` - Documentation guide for my hardware build.

---

## 🎮 How to Assemble (My Build Process)

1. **The Circuit Module:** Solder the 1N4148 matrix diodes and hot-swap sockets onto the underside back face of the custom PCB. Solder the Seeed Studio XIAO module onto its dedicated landing pads.
2. **Switch Plate Assembly:** Click all 16 Gateron switches directly into the 1.5mm grey switch plate, then firmly press the completed PCB against the bottom pins until they securely seat into the friction-fit hotswap contacts.
3. **Chassis Fitment:** Drop the unified switch/PCB module down onto the internal wall shelf step of the lower middle case walls.
4. **Final Clamping:** Drop the long machine screws up through the bottom
   
## 🖼️ Image of Gregory
   <img width="1211" height="763" alt="image" src="https://github.com/user-attachments/assets/02443119-c495-40e8-9124-9227335b2f02" />

## 🖼️ Image of Schematic
   <img width="1546" height="917" alt="image" src="https://github.com/user-attachments/assets/44d28559-8831-4a1d-8cb7-4fca484bffcc" />

## 🖼️ Image of PCB Design 
   <img width="841" height="852" alt="image" src="https://github.com/user-attachments/assets/483cf56c-722b-412b-81fd-442c3016c59a" />

## 🖼️ How to fit
   Top Plate can be fitted on top of the switch plate 
   <img width="1060" height="863" alt="image" src="https://github.com/user-attachments/assets/ef06e052-54de-4a54-8776-a2911f907f0a" />
   First PCB and switch plate are joined together and the switches places and then screwed on to the middle body from the top.(with an m2.2 screw)
   <img width="1098" height="808" alt="image" src="https://github.com/user-attachments/assets/35c289c4-defd-4aef-a999-c39f07b3da83" />
   The Base,Middle body and top plate are screwed form the bottom with an m.3 screw and it is 19 mm deep.
   <img width="1116" height="777" alt="image" src="https://github.com/user-attachments/assets/20dc03fb-dd1a-45ce-be83-f4336bf1d2ee" />
   The switch plate fits inside the the top plate so it looks clean but u can view the top screws from the top.Its to 3d print the same size curves and place then into 
   a arm rest or accessory as per preference.
   <img width="1470" height="632" alt="image" src="https://github.com/user-attachments/assets/ac24f95a-2684-4616-9d06-33d0b30fb317" />

## BOM 👀
1x 1 SEEEDUINO XIAO RP2040

16x Gateron KS-3X1 Milky Yellow Pro (https://stackskb.com/store/gateron-ks-3x1p-pro-yellows/)

1x SSD1327 128x128 Oled display (5V VCC, 3.3V logic, I2C)(https://www.waveshare.com/1.5inch-oled-module.htm)

18x N4148 Switching Diodes

16x Kailh Hotswap Switch Sockets

4x 19mm long m3 screws

4x 3mm long m2.2 screws

1x Rotatory Encoder(Without Switch cuz no switch pins)

1x WS2812B RGB LED Strip (Addressable underglow) (https://harishprojects.com/products/ws2812b-rgb-strip-light-programmable-pixel-led-light-5-meter-length?variant=45331583926450&country=IN&currency=INR&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&srsltid=AU7gw4WRh1LtbVOlv8bOb6F7SFyvggcoRjDHpNgGPT8EKlq-ODOOb_26jOY)






   

