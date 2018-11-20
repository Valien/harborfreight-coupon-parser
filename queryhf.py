#!/usr/local/bin python3

import requests

# https://images.harborfreight.com/hftweb/campaigns/localmedia/digitalsavings/Nov2018/digitalsavings_01.png'

BaseURL = 'https://images.harborfreight.com/hftweb/campaigns/localmedia/digitalsavings/'


def get_images(moyr, numimages):
    print('Acquiring images...')
    #urltoparse = BaseURL + my_input + '/digitalsavings_'

    for n in range(numimages):
            # urltoparse = BaseURL + my_input + \
                # '/digitalsavings_' + str(n).zfill(1) + ".png"
        if n < 10:
            #print(str(n).zfill(2))
            urltoparse = BaseURL + moyr + '/digitalsavings_' + str(n).zfill(2) + ".png"
            print(urltoparse)
            response = requests.get(urltoparse)  # + str(n))
            if response.status_code == 200:
                with open("/Users/allen.vailliencourt/Desktop/hf/" + moyr + '-' + str(n) + '.png', 'wb') as f:
                    f.write(response.content)
            else:
                print(f'Error! {response.status_code}')
        else:
            # print(n)
            urltoparse = BaseURL + moyr + '/digitalsavings_' + str(n) + ".png"
            print(urltoparse)
            # print(f'Parsing image {n}')
            response = requests.get(urltoparse)  # + str(n))
            if response.status_code == 200:
                with open("/Users/allen.vailliencourt/Desktop/hf/" + moyr + '-' + str(n) + '.png', 'wb') as f:
                    f.write(response.content)
            else:
                print(f'Error! {response.status_code}')

#def get_input():
my_input = input('Enter Month and Year in this format - Nov2018, Dec2018, etc.: ')
numrange_input = int(input('Enter range of numbers between 1-30: '))
print(f'You entered {my_input} for the month/year and a range of {numrange_input} for the amount of images to be downloaded.')
get_images(my_input, numrange_input)
    #print(f'Now parsing images from {BaseURL}\n')
    #print('All done!\n')
    #return (my_input, numrange_input)

#get_input()
#get_images()