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

The chassis is designed completely from scratch using **Onshape** using a highly rigid **Bottom-Up Sandwich Mount System**. 

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
2. **Switch Plate Assembly:** Click all 16 Leobog switches directly into the 1.5mm grey switch plate, then firmly press the completed PCB against the bottom pins until they securely seat into the friction-fit hotswap contacts.
3. **Chassis Fitment:** Drop the unified switch/PCB module down onto the internal wall shelf step of the lower middle case walls.
4. **Final Clamping:** Drop the long machine screws up through the bottom 
