import demosaicking 
import utils
import numpy as np
def main():
#    filename = 'kodak19.png'
#    filename = 'kodim01.png'
#    filename = 'barbara.jpg'
    filename = "goldhill.bmp"
    orimg = utils.getimg(filename)
    Ha = np.zeros((4,))
    Zhang = np.zeros((4,))
    # Mosaic image
    list_pattern = [[[0, 1], [1, 2]], [[2, 1], [1, 0]], [[1, 0], [2, 1]], [[1, 2], [0, 1]]]
    for pattern in list_pattern:
        mosaiced_img = utils.mosaicing(orimg, pattern)
        utils.array2img(mosaiced_img).save('hill_mosaic.png')
        
        # Demosaic by Hamilton-Adams method
        ha_demosaic = demosaicking.hamilton_demosaicing(mosaiced_img, pattern)
        utils.array2img(ha_demosaic).save('hill_ham.png')
        Ha += utils.PSNR(orimg, ha_demosaic, pattern)
        
        # Demosaic by LMMSE method
        lmmse_demosaic = demosaicking.LMMSE_demosaicing(mosaiced_img, pattern)
        utils.array2img(lmmse_demosaic).save('hill_zhang.jpg')
        Zhang += utils.PSNR(orimg, lmmse_demosaic, pattern)
#        utils.array2img(lmmse_demosaic[200:320,200:320]).show()
    # Print the PSNR results into a table
    print("Method         #  Red     #  Green    #  Blue     #  Image       #")
    print("Hamilton-Adams #  %.4f #  %.4f  #  %.4f  #  %.4f     #" % tuple(Ha/4))
    print("LMMSE          #  %.4f #  %.4f  #  %.4f  #  %.4f     #"% tuple(Zhang/4))
          

if __name__ == "__main__":
    main()
    
