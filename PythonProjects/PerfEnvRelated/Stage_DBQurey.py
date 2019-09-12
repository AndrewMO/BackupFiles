




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
        with open(r"/Users/ajia/Documents/tmp/STG_AddTaxSettings.txt", 'a+') as qurey:
            qurey.write("use " + "Activenetsites" + '\n')
            qurey.write("update ORGS set IS_TAX_EXEMPT = 0 where SITE_URL = " + "'" + db + "'" + '\n')
            qurey.write('\n')
            qurey.write("use " + db + '\n')
            qurey.write("if not exists (select keywordvalue from systeminfo where KEYWORD = 'tax_service_activated')" + '\n')
            qurey.write("BEGIN" + '\n')
            qurey.write("    insert into systeminfo (KEYWORD, KEYWORDVALUE)  values ('tax_service_activated', 'true')" + '\n')
            qurey.write("END" + '\n')
            qurey.write("else" + '\n')
            qurey.write("BEGIN" + '\n')
            qurey.write("    update systeminfo set keywordvalue = 'true' where keyword = 'tax_service_activated'" + '\n')
            qurey.write("END" + '\n')
            qurey.write('\n')




    with open(r"/Users/ajia/Documents/tmp/STG_AddTaxSettings.txt", 'a+') as qurey:
        qurey.write("use Activenetsites" + '\n')
        qurey.write("select SITE_URL, IS_TAX_EXEMPT from ORGS where SITE_URL in (" )
        for db in DB_Name:
            qurey.write("\'" + db +"\'")
            if db not in 'lstgymcasatx':
                qurey.write(", ")
        qurey.write(")" +'\n')

    with open(r"/Users/ajia/Documents/tmp/STG_AddTaxSettings.txt", 'a+') as qurey:
        for db in DB_Name:
            qurey.write("use " + db + '\n')
            qurey.write("select * from systeminfo where keyword = \'tax_service_activated\'" + '\n' )
            qurey.write('\n')






if __name__ == '__main__':
    main()