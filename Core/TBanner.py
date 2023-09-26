from colorama import Fore



_banner = '''
  #####                                     
 #     # #####  ###### #####  #    #   ##   
 #       #    # #      #    # ##  ##  #  #  
  #####  #    # #####  #    # # ## # #    # 
       # #####  #      #####  #    # ###### 
 #     # #      #      #   #  #    # #    # 
  #####  #      ###### #    # #    # #    # 
                                            
'''



def banner(host, port):
    '''Вывод баннера с ссылкой'''

    print(Fore.GREEN + _banner)
    print(f'Ссылка - http://{host}:{port}')
