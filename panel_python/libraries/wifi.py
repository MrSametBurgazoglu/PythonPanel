# -*- coding: utf-8 -*-

import wifi


def Search():
    wifilist = []

    cells = wifi.Cell.all('wlx74ea3a95f6a8')

    for cell in cells:
        wifilist.append(cell)

    return wifilist


def FindFromSearchList(ssid):
    wifilist = Search()

    for cell in wifilist:
        if cell.ssid == ssid:
            return cell

    return False


def FindFromSavedList(ssid):
    cell = wifi.Scheme.find('wlx74ea3a95f6a8', ssid)

    if cell:
        return cell

    return False


def Connect(ssid, password=None):
    cell = FindFromSearchList(ssid)
    print("a")
    if cell:
        savedcell = FindFromSavedList(cell.ssid)
        print("a")
        # Already Saved from Setting
        if savedcell:
            print("b")
            savedcell.activate()
            return cell

        # First time to conenct
        else:
            if cell.encrypted:
                print("a")
                print(password)
                if password:
                    scheme = Add(cell, password)
                    print("a")
                    try:
                        scheme.activate()
                    # Wrong Password
                    except wifi.exceptions.ConnectionError:
                        Delete(ssid)
                        return False

                    return cell
                else:
                    return False
            else:
                scheme = Add(cell)

                try:
                    scheme.activate()
                except wifi.exceptions.ConnectionError:
                    Delete(ssid)
                    return False

                return cell
    
    return False


def Add(cell, password=None):
    if not cell:
        return False

    scheme = wifi.Scheme.for_cell('wlx74ea3a95f6a8', cell.ssid, cell, password)
    scheme.save()
    return scheme


def Delete(ssid):
    if not ssid:
        return False

    cell = FindFromSavedList(ssid)

    if cell:
        cell.delete()
        return True

    return False
