import logging
import sys
import smpplib.gsm
import smpplib.client
import smpplib.consts
import os
from dotenv import load_dotenv

load_dotenv()
SMPP_IP = str(os.getenv("SMPP_IP"))
SMPP_PORT = int(os.getenv("SMPP_PORT"))
SMPP_USER = str(os.getenv("SMPP_USER"))
SMPP_PASS = str(os.getenv("SMPP_PASS"))
# if you want to know what's happening

def send_message(src,dest, string, client):

    parts, encoding_flag, msg_type_flag = smpplib.gsm.make_parts(string)

    logging.info('Sending SMS "%s" to %s' % (string, dest))
    for part in parts:
        pdu = client.send_message(
            source_addr_ton=smpplib.consts.SMPP_TON_ALNUM,
            source_addr_npi=smpplib.consts.SMPP_NPI_UNK,
            source_addr=src,
            dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
            dest_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
            destination_addr=dest,
            short_message=part,
            data_coding=encoding_flag,
            esm_class=msg_type_flag,
            registered_delivery=False,
    )




def send_sms_to_many(src, dest_list:list, message):
    logging.basicConfig(level='DEBUG')
    client = smpplib.client.Client(SMPP_IP, SMPP_PORT, allow_unknown_opt_params=True)

    # Print when obtain message_id
    client.set_message_sent_handler(
    lambda pdu: sys.stdout.write('sent {} {}\n'.format(pdu.sequence, pdu.message_id)))
    client.set_message_received_handler(
    lambda pdu: sys.stdout.write('delivered {}\n'.format(pdu.receipted_message_id)))

    client.connect()
    client.bind_transceiver(system_id=SMPP_USER, password=SMPP_PASS)
    for dest in dest_list:
        send_message(src,dest,message, client)