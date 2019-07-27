# -*- coding: utf-8 -*-

import geoip2.database
import logging

from flask import Flask, jsonify

logger = logging.getLogger(__name__)
reader = geoip2.database.Reader('GeoLite2-City.mmdb')

app = Flask(__name__)

@app.route('/<ip_address>')
def lookup(ip_address):
    response = reader.city(ip_address)

    attr_dicts = {
        'city': [
            'names',
            'geoname_id',
            'confidence',
        ],
        'continent': [
            'names',
            'geoname_id',
            'code',
        ],
        'country': [
            'is_in_european_union',
            'iso_code',
            'names',
            'confidence',
            'geoname_id',
        ],
        'location': [
            'time_zone',
            'metro_code',
            'longitude',
            'population_density',
            'postal_code',
            'average_income',
            'postal_confidence',
            'accuracy_radius',
            'latitude',
        ],
        'traits': [
            'is_tor_exit_node',
            'autonomous_system_number',
            'is_anonymous',
            'organization',
            'autonomous_system_organization',
            'is_anonymous_vpn',
            'user_type',
            'ip_address',
            'connection_type',
            'is_legitimate_proxy',
            'domain',
            'is_anonymous_proxy',
            'is_hosting_provider',
            'isp',
            'is_satellite_provider',
            'is_public_proxy',
        ],
    }

    data = {}

    for attr, fields in attr_dicts.items():
        obj = getattr(response, attr)
        data[attr] = {}

        for field in fields:
            data[attr][field] = getattr(obj, field)

    return jsonify(data)

if __name__ == '__main__':
    app.run(port = 5001)
