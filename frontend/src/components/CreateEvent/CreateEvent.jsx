import React from 'react'
import downArrow from '~/assets/img/down-arrow.svg'
function CreateEvent() {
  console.log(downArrow)
  return (
    <>
      <div className='wrapper'>
        <div className='heading'>
          <h1 className='main-heading'>Создание мероприятия</h1>
        </div>
        <div className='subheading'>
          <h2 className='main-subheading'>
            Вы можете создать одно или несколько мероприятий, чтобы потенциальне
            слушатели могли откликнуться.
          </h2>
        </div>
        <div className='cover-l label'> Обложка:</div>
        <div className='cover'>
          <img
            className='icon'
            src='assets/img/photo-icon.svg'
            alt='photo-icon'
          />
          <img
            className='title-img'
            src='https://via.placeholder.com/500'
            alt='placeholder'
          />
        </div>
        <div className='domain-l label'>Тематика:</div>
        <div className='domain'>
          <select
            className='domain-list'
            style={{ backgroundImage: `url(${downArrow})` }}
          >
            <option value='' disabled selected>
              Выберете тематику
            </option>
            <option value='opt1'>opt1</option>
            <option value='opt2'>opt2</option>
            <option value='opt3'>opt3</option>
          </select>
        </div>
        <div className='date-l label'>sdfsdf</div>
        <div className='date'>sdfsdf</div>
        <div className='time-l label'>sdfsdf</div>
        <div className='time'>sdfsdf</div>
        <div className='workspace-l label'>sdfsdf</div>
        <div className='workspace'>sdfsdf</div>
        <div className='address-l label'>sdfsdf</div>
        <div className='address'>sdfsdf</div>
        <div className='equip-l label'>sdfsdf</div>
        <div className='equip'>sdfsdf</div>
        <div className='desc-l label'>sdfsdf</div>
        <div className='desc'>sdfsdf</div>
        <div className='fee-l label'>sdfsdf</div>
        <div className='fee'>sdfsdf</div>
        <div className='submit'>sdfsdf</div>
      </div>
    </>
  )
}

export default CreateEvent
