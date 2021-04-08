#![no_std]
#![no_main]

#[no_mangle]
pub extern "C" fn _start() -> ! {
    let e: Result<(), ()> = Err(());
    e.unwrap();

    loop {}
}

#[panic_handler]
fn panic(_info: &core::panic::PanicInfo) -> ! {
    loop {}
}
