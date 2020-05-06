




def main():

    DB_Name = ['lstgapachejunction', 'lstgbreckenridgerec', 'lstgcampbellrecreation', 'lstgchandleraz',
               'lstgchesterfieldparksrec', 'lstgcityofcarlsbad', 'lstgcityofcorona', 'lstgcityofdowney',
               'lstgculpepercopandr', 'lstgdenver', 'lstgebparks', 'lstgencinitasparksandrec',
               'lstgfalmouthcommunityprog', 'lstgfpdccrecreation', 'lstggepark', 'lstggjparksandrec', 'lstgindymca',
               'lstgkansascityymca', 'lstglanguagestars', 'lstglbparks', 'lstgmesaaz', 'lstgminneapolisparks',
               'lstgmontgomerycounty', 'lstgmrurecreation', 'lstgnaparec', 'lstgnms', 'lstgnorthshoreymca',
               'lstgomahaconservatory', 'lstgoneteamkids', 'lstgportlandparks', 'lstgrightatschool',
               'lstgsanjoseparksandrec', 'lstgsdparkandrec', 'lstgsfcmprep', 'lstgymcagreaterbrandywine',
               'lstgymcasatx']


    # DB_Name = ['lstgapachejunction', 'lstgymcasatx']


    for db in DB_Name:
        with open(r"/Users/ajia/Documents/tmp/STG_CaptchaSettings.txt", 'a+') as qurey:
            qurey.write("use " + db + '\n')
            qurey.write("if not exists (select KEYWORDVALUE from dbo.systeminfo where keyword = 'enable_pci_captcha')" + '\n')
            qurey.write("BEGIN" + '\n')
            qurey.write("    insert into systeminfo (KEYWORD, KEYWORDVALUE)  values ('enable_pci_captcha', 'false')" + '\n')
            qurey.write("END" + '\n')
            qurey.write("else" + '\n')
            qurey.write("BEGIN" + '\n')
            qurey.write("    update systeminfo set keywordvalue = 'false' where keyword = 'enable_pci_captcha'" + '\n')
            qurey.write("END" + '\n')
            qurey.write("if not exists (select KEYWORDVALUE from dbo.systeminfo where keyword = 'enable_recaptcha')" + '\n')
            qurey.write("BEGIN" + '\n')
            qurey.write("    insert into systeminfo (KEYWORD, KEYWORDVALUE)  values ('enable_recaptcha', 'false')" + '\n')
            qurey.write("END" + '\n')
            qurey.write("else" + '\n')
            qurey.write("BEGIN" + '\n')
            qurey.write("    update systeminfo set keywordvalue = 'false' where keyword = 'enable_recaptcha'" + '\n')
            qurey.write("END" + '\n')
            qurey.write('\n')






if __name__ == '__main__':
    main()