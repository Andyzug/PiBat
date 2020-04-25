# PiBat
Battery Shield for Raspberry Pi 3/3B+ zero/w

RPI can read battery level and voltage from PiBat using i2c interface

The default Raspbian image disables I2C by default so before you can use it the interface must be enabled.

From the command line or Terminal window start by running the following command :

    sudo raspi-config

    This will launch the raspi-config utility. Select “Interfacing Options” 
    Highlight the “I2C” option and activate “<Select>”.
    Select and activate “<Yes>”
    Highlight and activate “<Ok>” :
    When prompted to reboot highlight and activate “<Yes>” 
    The Raspberry Pi will reboot and the interface will be enabled.
  

To help debugging and allow the interface to be used within Python we can install “python-smbus” and “i2c-tools” :

    sudo apt-get update
    sudo apt-get install -y python-smbus i2c-tools
  
Checking If I2C Is Enabled (Optional)

  When you power up or reboot your Pi you can check the i2c module is running by using the following command :

    lsmod | grep i2c_

  That will list all the modules starting with “i2c_”. If it lists “i2c_bcm2708” then the module is running correctly.
  
the i2cdetect  program will probe all the addresses on a bus, and report whether any devices are present.

    pi@raspberrypi:~/$ i2cdetect -y 1
         0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:          -- -- -- -- -- -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- 4d -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- --

If the adress is different than '4d' then modify file 'pibat.py' line 12

To use pibat.py, in terminal, navigate to it location and type:

    python pibat.py
    
THE END
                                    
                                    

