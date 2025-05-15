.syntax unified
.thumb
.global main
.type main, %function

main:
    bl init_leds              @ Initialize LEDs and GPIO pins

    ldr r6, =frame_list       @ r6 points to list of frames
    mov r7, #0                @ Frame index

loop_forever:
    ldr r4, [r6, r7, LSL #2]  @ r4 = address of current frame

    mov r8, #50               @ Repeat row multiplexing ~50 times per frame
show_frame_loop:
    mov r5, #0                @ r5 = row index

next_row:
    cmp r5, #5
    beq row_done

    ldrb r0, [r4, r5]         @ Load column pattern for current row
    bl write_column_pins

    mov r0, r5
    ldr r1, =OFS_GPIO_OUT
    mov r2, #1
    bl write_row_pin

    bl short_delay            @ Brief delay for this row

    mov r0, r5
    ldr r1, =OFS_GPIO_OUT
    mov r2, #0
    bl write_row_pin

    add r5, r5, #1
    b next_row

row_done:
    subs r8, r8, #1
    bne show_frame_loop

    bl frame_delay            @ Longer delay before moving to next frame

    add r7, r7, #1
    cmp r7, #8                @ Total number of frames
    bne loop_forever
    mov r7, #0
    b loop_forever

short_delay:
    ldr r0, =3000
short_delay_loop:
    subs r0, #1
    bne short_delay_loop
    bx lr

frame_delay:
    ldr r0, =2000000
frame_delay_loop:
    subs r0, #1
    bne frame_delay_loop
    bx lr

.size main, .-main

.data
square:
    .byte 0b00000
    .byte 0b00000
    .byte 0b00000
    .byte 0b00000
    .byte 0b00000

inbox:
    .byte 0b11111
    .byte 0b10001
    .byte 0b10101
    .byte 0b10001
    .byte 0b01110

diagonal_box:
    .byte 0b01110
    .byte 0b01010
    .byte 0b00100
    .byte 0b01010
    .byte 0b01110

outbox:
    .byte 0b00000
    .byte 0b01110
    .byte 0b01110
    .byte 0b01110
    .byte 0b00000

line1:
    .byte 0b00000
    .byte 0b11111
    .byte 0b11111
    .byte 0b11111
    .byte 0b00000

line2:
    .byte 0b11111
    .byte 0b00000
    .byte 0b11111
    .byte 0b00000
    .byte 0b11111

line3:
    .byte 0b11111
    .byte 0b11111
    .byte 0b00000
    .byte 0b11111
    .byte 0b11111

sad_face:
    .byte 0b11111
    .byte 0b10101
    .byte 0b11111
    .byte 0b10001
    .byte 0b01110

frame_list:
    .word square
    .word inbox
    .word outbox
    .word diagonal_box
    .word line1
    .word line2
    .word line3
    @ .word sad_face