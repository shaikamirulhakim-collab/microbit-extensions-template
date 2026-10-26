def on_sugar_rfid_tag_detected():
    basic.show_icon(IconNames.YES)
    music.play(music.string_playable("C5 B A G F E D C ", 120),
        music.PlaybackMode.UNTIL_DONE)
    Sugar.sugar_rfid_write_block(Sugar.sugar_rfid_read_uid(), 0)
    OledKitten.clear()
Sugar.sugar_rfid_on_tag_detected(on_sugar_rfid_tag_detected)

SCD40.start_continuous_measurement()
basic.show_string("" + str((SCD40.get_temperature(SCD40.SCD40_T_UNIT.C))))
basic.show_string("" + str((SCD40.get_co2())))
basic.show_string("" + str((SCD40.get_relative_humidity())))
SCD40.stop_continuous_measurement()
strip = neopixel.create(DigitalPin.P1, 32, NeoPixelMode.RGB)
if input.button_is_pressed(Button.A):
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P12, 0)
elif input.button_is_pressed(Button.B):
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P12, 1)
    strip = neopixel.create(DigitalPin.P1, 32, NeoPixelMode.RGB)
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P0, True, False, True)
    if dht11_dht22.read_data(dataType.HUMIDITY) > 50:
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    else:
        strip.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
elif input.button_is_pressed(Button.AB):
    basic.show_icon(IconNames.HEART)
elif input.logo_is_pressed():
    strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
else:
    strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)