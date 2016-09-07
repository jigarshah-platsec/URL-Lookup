#!/usr/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import cgi
import re
from Malware_Db_Info import TABLES
from Malware_Db_Info import DB_NAME
from Malware_Db_Info import TABLE_NAME
from Malware_Db_Info import config
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)


class URL_Lookup:

    def __init__(self, URL):
        self.URL = URL

    def lookup(self):
        """
        Regex to Match URL in various format
        This would match cases like:
        www.google.com
        https://www.google.com
        http://net.tutsplus.com/about
        Detail: http://code.tutsplus.com/tutorials/8-regular-expressions-you-should-know--net-6149
        """
        regex = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'

        # Grep the domain from input URL to match against db
        match = re.search(regex, self.URL)

        Domain = ""
        MalwareURL = True
        if match:
            Domain = match.group(2) + "." + match.group(3)
        else:
            print ("Enter valid URL in format (http://www.google.com)")
            raise

        # Connect db and search the domain is in list of malwares
        link = mysql.connector.connect(**config)
        cursor = link.cursor()
        try:
            link.database = DB_NAME
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                exit(1)

        print("Successful connection")
        print Domain
        query = "SELECT COUNT(*) FROM malwares where malware = '{0}'".format(Domain)
        print query
        cursor.execute(query)
        MalwareURL, = cursor.fetchone()

        """
        with open("simple_malware.txt") as f:
            for line in f:
                if re.search(Domain, line):
                    MalwareURL = False
                    break
        """

        # Response format
        # TODO: Change response as a JSON {validated: "True"/"False"} 
        if MalwareURL:
            return True
        else:
            return False
