#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

import qi
import argparse
import sys
import time


def main(robot_session):

    # Get the service ALTabletService.

    try:
        tabletService = robot_session.service("ALTabletService")

        # Display the index.html page of a behavior name j-tablet-browser
        # The index.html must be in a folder html in the behavior folder
        tabletService.loadApplication("projet_accueil")
        tabletService.showWebview()
        enCours = 1;
        while (int(enCours)):
            enCours = raw_input("Entrer 0 pour terminer!")
        

        # Hide the web view
        tabletService.hideWebview()
    except Exception, e:
        print "Error was: ", e


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="134.214.50.49",
                        help="Robot IP address. On robot or Local Naoqi: use '134.214.50.49'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    robot_session = qi.Session()
    try:
        robot_session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"+"Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(robot_session)
