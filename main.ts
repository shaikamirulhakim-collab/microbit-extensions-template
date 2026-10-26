Sugar.sugarRfidOnTagDetected(function () {
    basic.showIcon(IconNames.Yes)
    music.play(music.stringPlayable("C5 B A G F E D C ", 120), music.PlaybackMode.UntilDone)
    Sugar.sugarRfidWriteBlock(Sugar.sugarRfidReadUid(), 0)
    OledKitten.clear()
})
SCD40.start_continuous_measurement()
basic.showString("" + (SCD40.get_temperature(SCD40.SCD40_T_UNIT.C)))
basic.showString("" + (SCD40.get_co2()))
basic.showString("" + (SCD40.get_relative_humidity()))
SCD40.stop_continuous_measurement()
let strip = neopixel.create(DigitalPin.P1, 32, NeoPixelMode.RGB)
if (input.buttonIsPressed(Button.A)) {
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P12, 0)
} else if (input.buttonIsPressed(Button.B)) {
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P12, 1)
    strip = neopixel.create(DigitalPin.P1, 32, NeoPixelMode.RGB)
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P0,
    true,
    false,
    true
    )
    if (dht11_dht22.readData(dataType.humidity) > 50) {
        strip.showColor(neopixel.colors(NeoPixelColors.Blue))
    } else {
        strip.showColor(neopixel.colors(NeoPixelColors.Indigo))
    }
    strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
} else if (input.buttonIsPressed(Button.AB)) {
    basic.showIcon(IconNames.Heart)
} else if (input.logoIsPressed()) {
    strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
} else {
    strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
}
