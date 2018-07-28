MOV_R4R0_LDR_R1R0_LDR_R1R1_8_BLX_R1 = 0x216000
LDRD_R2R3R0_60_LDR_R0R0_LDR_R1R0_34_MOV_R0R4_BLX_R1 = 0x1F615C
LDRD_ROR1R4_8_BLX_R2 = 0x11E740

MOV_SPR0_MOV_R0R2_MOV_LRR3_BX_R1 = 0x16E978

NOP = 0x297DFC
POP_R0PC = 0x10FBE4
POP_R1PC = 0x28BE28
POP_R3PC = 0x117D10
POP_R4PC = 0x1042B8
POP_R4R5PC = 0x108284
POP_R4R5R6PC = 0x104264
POP_R2R3R4R5R6PC = 0x277C10
POP_R4R5R6R7R8R9R10R11R12PC = 0x29C95C

POP_R4LR_BX_R1 = 0x12355C

SUB_SPSP_BC_LDR_R3R0_MUL_R1R7R1_LDR_R3R3_8_BLX_R3 = 0x393144

LDR_R0R0_POP_R4PC = 0x20D778
LDR_R0R4_POP_R4PC = 0x13897C
STR_R0R4_POP_R4PC = 0x1301FC
ADD_R0R0R4_POP_R4R5R6PC = 0x12C1A4
ADD_R0R0R1_POP_R4PC = 0x18BC28

CMP_R0_0_MOVNE_R0_1_POP_R4PC = 0x10FD38
STREQ_R0R4_4_POP_R4R5R6PC = 0x37568C

MEMCPY = 0x28B954
MEMCMP = 0x259914

SVC_SLEEPTHREAD = 0x273D6C
SVC_EXITTHREAD = 0x11E76C

GSPGPU_GXTRYENQUEUE_WRAPPER = 0x120A00
GSPGPU_GXTRYENQUEUE = 0x278A34
GSPGPU_SETTEXTURECOPY = 0x120C70 #GXCMD4
GSPGPU_FLUSHDATACACHE_WRAPPER = 0x118A10
GSPGPU_FLUSHDATACACHE = 0x120F94
GSPGPU_INTERRUPT_RECEIVER_STRUCT = 0x3EDC40
GSPGPU_HANDLE = 0x3F67F0

DSP_UNLOADCOMPONENT = 0x278C1C
DSP_REGISTERINTERRUPTEVENTS = 0x2FB604
DSP_HANDLE = 0x3F67B4

#OFFSET/PTR
SECTION1_OFFSET = 0xE8
SECTION2_OFFSET = 0x2E348
SECTION1_PTR = 0x08A67E84
FILE_PTR = SECTION1_PTR - SECTION1_OFFSET
SECTION2_PTR = FILE_PTR + SECTION2_OFFSET
OTHERAPP_PTR = FILE_PTR+0x190000+0x4

DWORD_3F0E1C = 0x425580
BUTTON_TABLE = DWORD_3F0E1C + 0x19FC + 0x50

ROP_PTR = FILE_PTR+0x160000
CODE_PTR = FILE_PTR+0x170000
STACK_DEST = 0x0FFFFEF4

ANNOYING_THREAD_KILL = 0x4FA3B8
