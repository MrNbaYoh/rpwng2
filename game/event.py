import itertools
include("../ropdb/DB.py")

def u32_to_byte_list(u32):
	return [(u32 & (0xFF << 8*i)) >> 8*i for i in range(4)]

def u32_array_to_bits_array(l):
	L = []
	for u32 in l:
		for b in u32_to_byte_list(u32):
			for i in range(8):
				L.append((b & (1 << i)) >> i)
	return L

def bits_array_to_bits_count(l):
	return [(b, len(list(i))) for b, i in itertools.groupby(l)]

def make_event_list(l, addr):
	l = bits_array_to_bits_count(u32_array_to_bits_array(l))
	event_list = [0X2D, 0x00, 0xFF, 0xFF, 0x04, 0x00, 0x0C, 0x00, 0, 0, 0, 0, 0, 0, 0, 0]*len(l)
	k = 0
	for b, c in l:
		index = (addr - BUTTON_TABLE) * 8
		event_list += [0x01, 0xFF, 0xFF, 0x0F]
		event_list += [b, int(c > 1), 0x00, 0x00]
		event_list += u32_to_byte_list(index + k)
		event_list += u32_to_byte_list(index + k + c - 1)
		k += c
	return event_list, len(l)
