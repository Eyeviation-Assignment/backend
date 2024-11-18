import logging
import traceback
from http import HTTPStatus

from flask import Blueprint

from DTOs.exception_dto import ExceptionDTO
from exceptions.bad_request_exception import BadRequestException

error_handler_bp = Blueprint('error_handler', __name__)


@error_handler_bp.app_errorhandler(Exception)
def general_exception(e: Exception):
    logging.error(f'Internal server error. Exception type: {type(e)}. Exception message: {str(e)}')
    logging.error(traceback.format_exc())
    return ExceptionDTO(HTTPStatus.INTERNAL_SERVER_ERROR.value, 'Internal Server Error').to_dict(), HTTPStatus.INTERNAL_SERVER_ERROR.value


# @error_handler_bp.app_errorhandler(InvalidCredentialsException)
# @error_handler_bp.app_errorhandler(Unauthorized)
# def not_found_exception(e: InvalidCredentialsException):
#     error_message: str = str(e)
#     if isinstance(e, Unauthorized):
#         error_message = 'check your credentials.'
#     logging.error(f'Unauthorized. Exception type: {type(e)}. Exception message: {error_message}')
#     return ExceptionDTO(HTTPStatus.UNAUTHORIZED.value, 'Unauthorized', error_message).to_dict(), HTTPStatus.UNAUTHORIZED.value
#
#
# @error_handler_bp.app_errorhandler(ForbiddenException)
# def forbidden_exception(e: InvalidCredentialsException):
#     logging.error(f'Forbidden. Exception type: {type(e)}. Exception message: {str(e)}')
#     return ExceptionDTO(HTTPStatus.FORBIDDEN.value, 'Forbidden', str(e)).to_dict(), HTTPStatus.FORBIDDEN.value
#
#
# @error_handler_bp.app_errorhandler(NotFoundException)
# def not_found_exception(e: NotFoundException):
#     logging.error(f'Resource Not found. Exception type: {type(e)}. Exception message: {str(e)}')
#     return ExceptionDTO(HTTPStatus.NOT_FOUND.value, 'Resource Not found', str(e)).to_dict(), HTTPStatus.NOT_FOUND.value


@error_handler_bp.app_errorhandler(BadRequestException)
def bad_request_exception(e: BadRequestException):
    logging.error(f'Bad Request. Exception type: {type(e)}. Exception message: {str(e)}')
    return ExceptionDTO(HTTPStatus.BAD_REQUEST.value, 'Bad Request', str(e)).to_dict(), HTTPStatus.BAD_REQUEST.value


# @error_handler_bp.app_errorhandler(DuplicatedException)
# @error_handler_bp.app_errorhandler(IntegrityError)  # not only duplicated error, should separate
# def duplicated_exception(e: Union[DuplicatedException, IntegrityError]):
#     error_message: str = str(e)
#     if isinstance(e, IntegrityError):
#         logging.error(f'Integrity error full message: {str(e)}')
#         error_message = 'Duplicated DB record.'
#     logging.error(f'Conflict. Exception type: {type(e)}. Exception message: {error_message}')
#     return ExceptionDTO(HTTPStatus.CONFLICT.value, 'Conflict', error_message).to_dict(), HTTPStatus.CONFLICT.value
