include("event.py")
include("../ropdb/DB.py")
import os

event_list, count = make_event_list([POP_R0PC, ROP_PTR, POP_R1PC, NOP, MOV_SPR0_MOV_R0R2_MOV_LRR3_BX_R1], STACK_DEST)

incbin("bins/file_0.bin")
add_word(len(event_list) + 0x46C) # sample map size

incbin("bins/file_1.bin")
add_word(count)

incbin("bins/event_opt.bin")

append(event_list)

org(0x160000)
incbin("../rop/build/rop.bin")

org(0x170000)
incbin("../code/code.bin")

org(0x190000)
add_word(os.path.getsize('../otherapp.bin'))
incbin("../otherapp.bin")

