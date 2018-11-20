#!/usr/local/bin python3

import requests

# https://images.harborfreight.com/hftweb/campaigns/localmedia/digitalsavings/Nov2018/digitalsavings_01.png'

BaseURL = 'https://images.harborfreight.com/hftweb/campaigns/localmedia/digitalsavings/'


def get_images(moyr, numimages):
    print('Acquiring images...')
    
    for n in range(numimages):
        ''' 
            This function get's the images. Yar! Does require you to enter Month and Number of images.
        '''    
        if n < 10:
            urltoparse = BaseURL + moyr + '/digitalsavings_' + str(n).zfill(2) + ".png"
            print(urltoparse)
            response = requests.get(urltoparse)  # + str(n))
            if response.status_code == 200:
                # to do: remove my hard-coded desktop location...
                with open("/Users/allen.vailliencourt/Desktop/hf/" + moyr + '-' + str(n) + '.png', 'wb') as f:
                    f.write(response.content)
            else:
                print(f'Error! {response.status_code}')
        else:
            urltoparse = BaseURL + moyr + '/digitalsavings_' + str(n) + ".png"
            print(urltoparse)
            response = requests.get(urltoparse)
            if response.status_code == 200:
                # to do: see above.
                with open("/Users/allen.vailliencourt/Desktop/hf/" + moyr + '-' + str(n) + '.png', 'wb') as f:
                    f.write(response.content)
            else:
                print(f'Error! {response.status_code}')

my_input = input('Enter Month and Year in this format - Nov2018, Dec2018, etc.: ')
numrange_input = int(input('Enter range of numbers between 1-30: '))
print(f'You entered {my_input} for the month/year and a range of {numrange_input} for the amount of images to be downloaded.')
#print(f'Now parsing images from {BaseURL}\n')
#print('All done!\n')
get_images(my_input, numrange_input)

